import copy, itertools, json, logging
import torch
from torch.utils.data import Dataset
from collections import Counter, namedtuple, defaultdict
from .graph import Graph
from .util import read_ltf, read_txt, read_json, read_json_single
import ipdb

logger = logging.getLogger(__name__)

instance_fields = [
    'doc_id', 'wnd_id', 'sent_id', 'tokens', 'pieces', 'piece_idxs', 'token_lens', 'attention_mask',
    'entity_label_idxs', 'trigger_label_idxs',
    'entity_type_idxs', 'event_type_idxs',
    'relation_type_idxs', 'role_type_idxs',
    'mention_type_idxs',
    'graph', 'entity_num', 'trigger_num'
]
instance_ldc_eval_fields = [
    'sent_id', 'tokens', 'token_ids', 'pieces', 'piece_idxs',
    'token_lens', 'attention_mask'
]
batch_fields = [
    'doc_ids', 'wnd_ids', 'sent_ids', 'tokens', 'piece_idxs', 'token_lens', 'attention_masks',
    'entity_label_idxs', 'trigger_label_idxs',
    'entity_type_idxs', 'event_type_idxs', 'mention_type_idxs',
    'relation_type_idxs', 'role_type_idxs',
    'graphs', 'token_nums'
]
batch_ldc_eval_fields = [
    'sent_ids', 'token_ids', 'tokens', 'piece_idxs', 'token_lens', 'attention_masks', 'token_nums'
]
Instance = namedtuple('Instance', field_names=instance_fields,
                      defaults=[None] * len(instance_fields))
InstanceLdcEval = namedtuple('InstanceLdcEval',
                             field_names=instance_ldc_eval_fields,
                             defaults=[None] * len(instance_ldc_eval_fields))
Batch = namedtuple('Batch', field_names=batch_fields,
                   defaults=[None] * len(batch_fields))
BatchLdcEval = namedtuple('BatchLdcEval',
                          field_names=batch_ldc_eval_fields,
                          defaults=[None] * len(batch_ldc_eval_fields))
BatchEval = namedtuple('BatchEval', field_names=['sent_ids', 'piece_idxs',
                                                 'tokens', 'attention_masks',
                                                 'token_lens', 'token_nums'])


def remove_overlap_entities(entities, token_num):
    """There are a few overlapping entities in the data set. We only keep the
    first one and map others to it.
    :param entities (list): a list of entity mentions.
    :return: processed entity mentions and a table of mapped IDs.
    """
    tokens = [None] * 1000
    entities_ = []
    id_map = {}
    for entity in entities:
        start, end = entity['start'], entity['end']
        if end > token_num:
            continue
        for i in range(start, end):
            if tokens[i]:
                id_map[entity['id']] = tokens[i]
                continue
        entities_.append(entity)
        for i in range(start, end):
            tokens[i] = entity['id']
    return entities_, id_map


def get_entity_labels(entities, token_num):
    """Convert entity mentions in a sentence to an entity label sequence with
    the length of token_num
    CHECKED
    :param entities (list): a list of entity mentions.
    :param token_num (int): the number of tokens.
    :return:a sequence of BIO format labels.
    """
    labels = ['O'] * token_num
    for entity in entities:
        start, end = entity['start'], entity['end']
        #if end > token_num:
        #    continue
        entity_type = entity.get('entity_type', "UNK")
        if any([labels[i] != 'O' for i in range(start, end)]):
            continue
        labels[start] = 'B-{}'.format(entity_type)
        for i in range(start + 1, end):
            labels[i] = 'I-{}'.format(entity_type)
    return labels


def get_trigger_labels(events, token_num):
    """Convert event mentions in a sentence to a trigger label sequence with the
    length of token_num.
    :param events (list): a list of event mentions.
    :param token_num (int): the number of tokens.
    :return: a sequence of BIO format labels.
    """
    labels = ['O'] * token_num
    for event in events:
        trigger = event['trigger']
        start, end = trigger['start'], trigger['end']
        event_type = event['event_type']
        #if end > token_num:
        #    continue
        labels[start] = 'B-{}'.format(event_type)
        for i in range(start + 1, end):
            labels[i] = 'I-{}'.format(event_type)
    return labels


def get_relation_types(entities, relations, id_map, under_test, vocab,
                    directional=False, symmetric=None):
    """Get relation type labels among all entities in a sentence.
    :param entities (list): a list of entity mentions.
    :param relations (list): a list of relation mentions.
    :param id_map (dict): a dict of entity ID mapping.
    :param symmetric (set): a set of symmetric relation types.
    :return: a matrix of relation type labels.
    """
    entity_num = len(entities)
    labels = [['O'] * entity_num for _ in range(entity_num)]
    entity_idxs = {entity['id']: i for i, entity in enumerate(entities)}
    for relation in relations:
        entity_1 = entity_2 = -1
        for arg in relation['arguments']:
            entity_id = arg['entity_id']
            entity_id = id_map.get(entity_id, entity_id)
            if arg['role'] == 'Arg-1' and entity_id in entity_idxs.keys():
                entity_1 = entity_idxs[entity_id]
            elif arg['role'] == 'Arg-2' and entity_id in entity_idxs.keys():
                entity_2 = entity_idxs[entity_id]
        if entity_1 == -1 or entity_2 == -1:
            continue
        if under_test and relation['relation_type'] not in vocab.keys():
            labels[entity_1][entity_2] = 'O'
        else:
            labels[entity_1][entity_2] = relation['relation_type']
            if not directional:
                labels[entity_2][entity_1] = relation['relation_type']
            if symmetric and relation['relation_type'] in symmetric:
                labels[entity_2][entity_1] = relation['relation_type']
    return labels


def get_relation_list(entities, relations, id_map, vocab, under_test,
                    directional=False, symmetric=None):
    """Get the relation list (used for Graph objects)
    :param entities (list): a list of entity mentions.
    :param relations (list): a list of relation mentions.
    :param id_map (dict): a dict of entity ID mapping.
    :param vocab (dict): a dict of label to label index mapping.
    """
    entity_idxs = {entity['id']: i for i, entity in enumerate(entities)}
    visited = [[0] * len(entities) for _ in range(len(entities))]
    relation_list = []
    for relation in relations:
        arg_1 = arg_2 = None
        for arg in relation['arguments']:
            entity_id = arg['entity_id']
            entity_id = id_map.get(entity_id, entity_id)
            if arg['role'] == 'Arg-1' and entity_id in entity_idxs.keys():
                arg_1 = entity_idxs[entity_id]
            elif arg['role'] == 'Arg-2' and entity_id in entity_idxs.keys():
                arg_2 = entity_idxs[entity_id]
        if arg_1 is None or arg_2 is None:
            continue
        if under_test and relation['relation_type'] not in vocab.keys():
            continue
        else:
            relation_type = relation['relation_type']
        if (not directional and arg_1 > arg_2) or \
                (directional and symmetric and relation_type in symmetric and arg_1 > arg_2):
            arg_1, arg_2 = arg_2, arg_1
        if visited[arg_1][arg_2] == 0:
            relation_list.append((arg_1, arg_2, vocab[relation_type]))
            visited[arg_1][arg_2] = 1

    relation_list.sort(key=lambda x: (x[0], x[1]))
    return relation_list


def get_role_types(entities, events, id_map, vocab, under_test):
    labels = [['O'] * len(entities) for _ in range(len(events))]
    entity_idxs = {entity['id']: i for i, entity in enumerate(entities)}
    for event_idx, event in enumerate(events):
        for arg in event['arguments']:
            entity_id = arg['entity_id']
            entity_id = id_map.get(entity_id, entity_id)
            entity_idx = entity_idxs.get(entity_id, None)
            if entity_idx is None:
                continue
            # if labels[event_idx][entity_idx] != 'O':
            #     print('Conflict argument role {} {} {}'.format(event['trigger']['text'], arg['text'], arg['role']))
            if under_test and arg['role'] not in vocab.keys():
                labels[event_idx][entity_idx] = 'O'
            else:
                labels[event_idx][entity_idx] = arg['role']
    return labels


def get_role_list(entities, events, id_map, vocab, under_test=False):
    entity_idxs = {entity['id']: i for i, entity in enumerate(entities)}
    visited = [[0] * len(entities) for _ in range(len(events))]
    role_list = []
    for i, event in enumerate(events):
        for arg in event['arguments']:
            entity_idx = entity_idxs.get(id_map.get(
                arg['entity_id'], arg['entity_id']), None)
            if entity_idx is None:
                continue
            if visited[i][entity_idx] == 0:
                if under_test and arg['role'] not in vocab.keys():
                    #role_list.append((i, entity_idx, vocab['O']))
                    continue
                role_list.append((i, entity_idx, vocab[arg['role']]))
                visited[i][entity_idx] = 1
    role_list.sort(key=lambda x: (x[0], x[1]))
    return role_list


def get_coref_types(entities):
    entity_num = len(entities)
    labels = [['O'] * entity_num for _ in range(entity_num)]
    clusters = defaultdict(list)
    for i, entity in enumerate(entities):
        entity_id = entity['entity_id']
        cluster_id = entity_id[:entity_id.rfind('-')]
        clusters[cluster_id].append(i)
    for _, entities in clusters.items():
        for i, j in itertools.combinations(entities, 2):
            labels[i][j] = 'COREF'
            labels[j][i] = 'COREF'
    return labels


def get_coref_list(entities, vocab):
    clusters = defaultdict(list)
    coref_list = []
    for i, entity in enumerate(entities):
        entity_id = entity['entity_id']
        cluster_id = entity_id[:entity_id.rfind('-')]
        clusters[cluster_id].append(i)
    for _, entities in clusters.items():
        for i, j in itertools.combinations(entities, 2):
            if i < j:
                coref_list.append((i, j, vocab['COREF']))
            else:
                coref_list.append((j, i, vocab['COREF']))
    coref_list.sort(key=lambda x: (x[0], x[1]))
    return coref_list


def merge_coref_relation_lists(coref_list, relation_list, entity_num):
    visited = [[0] * entity_num for _ in range(entity_num)]
    merge_list = []
    for i, j, l in coref_list:
        visited[i][j] = 1
        visited[j][i] = 1
        merge_list.append((i, j, l))
    for i, j, l in relation_list:
        assert visited[i][j] == 0 and visited[j][i] == 0
        merge_list.append((i, j, l))
    merge_list.sort(key=lambda x: (x[0], x[1]))


def merge_coref_relation_types(coref_types, relation_types):
    entity_num = len(coref_types)
    labels = copy.deepcopy(coref_types)
    for i in range(entity_num):
        for j in range(entity_num):
            label = relation_types[i][j]
            if label != 0:
                assert labels[i][j] == 0
                labels[i][j] = label
    return labels


class IEDataset(Dataset):
    def __init__(self, raw_data, tokenizer, max_length=128, gpu=False, ignore_title=False,
                 relation_mask_self=True, relation_directional=False,
                 coref=False, symmetric_relations=None, test=False):
        self.raw_data = raw_data
        self.data = []
        self.gpu = gpu
        self.max_length = max_length
        self.ignore_title = ignore_title
        self.relation_mask_self = relation_mask_self
        self.relation_directional = relation_directional
        self.coref = coref
        if symmetric_relations is None:
            self.symmetric_relations = set()
        else:
            self.symmetric_relations = symmetric_relations
        self.tokenizer = tokenizer
        self.test = test
        self.load_data()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    @property
    def entity_type_set(self):
        type_set = set()
        for inst in self.data:
            for entity in inst['entity_mentions']:
                type_set.add(entity.get('entity_type', "UNK"))
        return type_set

    @property
    def event_type_set(self):
        type_set = set()
        for inst in self.data:
            for event in inst['event_mentions']:
                type_set.add(event['event_type'])
        return type_set

    @property
    def relation_type_set(self):
        type_set = set()
        for inst in self.data:
            for relation in inst.get('relation_mentions', []):
                type_set.add(relation['relation_type'])
        return type_set

    @property
    def role_type_set(self):
        type_set = set()
        for inst in self.data:
            for event in inst['event_mentions']:
                for arg in event['arguments']:
                    type_set.add(arg['role'])
        return type_set

    def load_data(self):
        overlength_num = 0
        for inst in self.raw_data:
            
            ## added
            pieces = [self.tokenizer.tokenize(t, is_split_into_words=True) for t in inst['tokens']]
            token_lens = [len(x) for x in pieces]
            if 0 in token_lens:
                raise ValueError
            pieces = [p for ps in pieces for p in ps]
            inst['pieces'] = pieces
            inst['token_lens'] = token_lens
            
            inst['entity_mentions'] = inst['extra_info']['entity_mentions']
            inst['relation_mentions'] = inst['extra_info']['relation_mentions']
            inst['event_mentions'] = inst['extra_info']['event_mentions']
            ##

            if not self.test:
                if self.max_length != -1 and len(pieces) > self.max_length - 2:
                    overlength_num += 1
                    continue
            else:
                if len(pieces) > self.max_length - 2:
                    # add token_lens until over-length
                    piece_counter = 0
                    for max_token_include, token_len in enumerate(inst['token_lens']):
                        if piece_counter + token_len >= self.max_length - 2:
                            logger.info('overlength during testing...')
                            break
                        else:
                            piece_counter += token_len
                    inst['pieces'] = inst['pieces'][:piece_counter]
                    inst['token_lens'] = inst['token_lens'][:max_token_include]
                    inst['tokens'] = inst['tokens'][:max_token_include]
            self.data.append(inst)

        if overlength_num:
            logger.info('Discarded {} overlength instances'.format(overlength_num))
        logger.info('Loaded {} OneIE instances from {} E2E instances'.format(len(self), len(self.raw_data)))

    def numberize(self, tokenizer, vocabs):
        """Numberize word pieces, labels, etcs.
        :param tokenizer: Bert tokenizer.
        :param vocabs (dict): a dict of vocabularies.
        """
        entity_type_stoi = vocabs.get('entity_type', None)
        event_type_stoi = vocabs.get('event_type', None)
        relation_type_stoi = vocabs.get('relation_type', None)
        role_type_stoi = vocabs.get('role_type', None)
        mention_type_stoi = vocabs.get('mention_type', None)
        entity_label_stoi = vocabs.get('entity_label', None)
        trigger_label_stoi = vocabs.get('trigger_label', None)

        data = []
        for inst in self.data:
            doc_id = inst['doc_id']
            wnd_id = inst['wnd_id']
            tokens = inst['tokens']
            pieces = inst['pieces']
            sent_id = inst['wnd_id']
            entities = inst['entity_mentions']
            token_num = len(tokens)
            entities, entity_id_map = remove_overlap_entities(entities, token_num)
            entities.sort(key=lambda x: x['start'])
            events = inst['event_mentions']
            events.sort(key=lambda x: x['trigger']['start'])
            events = [eve for eve in events if eve['trigger']['end']<= token_num]
            relations = inst.get('relation_mentions', [])
            token_lens = inst['token_lens']

            # Pad word pieces with special tokens
            piece_idxs = tokenizer.encode(pieces,
                                          add_special_tokens=True,
                                          max_length=self.max_length,
                                          truncation=True)
            pad_num = self.max_length - len(piece_idxs)
            attn_mask = [1] * len(piece_idxs) + [0] * pad_num
            #piece_idxs = piece_idxs + [0] * pad_num
            pad_id = self.tokenizer.convert_tokens_to_ids(self.tokenizer.pad_token)
            piece_idxs = piece_idxs + [pad_id] * pad_num
            
            # Entity
            # - entity_labels and entity_label_idxs are used for identification
            # - entity_types and entity_type_idxs are used for classification
            # - entity_list is used for graph representation
            entity_labels = get_entity_labels(entities, token_num)
            entity_label_idxs = [entity_label_stoi[l] for l in entity_labels]
            entity_types = [e.get('entity_type', "UNK") for e in entities]
            entity_type_idxs = [entity_type_stoi[l] for l in entity_types]
            entity_list = [(e['start'], e['end'], entity_type_stoi[e.get('entity_type', "UNK")])
                           for e in entities]
            # entity_num = len(entity_list)
            mention_types = [e.get('mention_type', "UNK") for e in entities]
            mention_type_idxs = [mention_type_stoi[l] for l in mention_types]
            mention_list = [(i, j, l) for (i, j, k), l
                            in zip(entity_list, mention_type_idxs)]

            # Trigger
            # - trigger_labels and trigger_label_idxs are used for identification
            # - event_types and event_type_idxs are used for classification
            # - trigger_list is used for graph representation
            trigger_labels = get_trigger_labels(events, token_num)
            if self.test:
                trigger_label_idxs = []
                for l in trigger_labels:
                    if l in trigger_label_stoi.keys():
                        trigger_label_idxs.append(trigger_label_stoi[l])
                    else:
                        trigger_label_idxs.append(trigger_label_stoi['O']) # we need this when xl test
                event_type_idxs = [event_type_stoi[e['event_type']] for e in events 
                                    if (e['trigger']['end'] <= token_num) and (e['event_type'] in event_type_stoi.keys())]
                trigger_list = [(e['trigger']['start'], e['trigger']['end'],
                                event_type_stoi[e['event_type']])
                                for e in events if e['event_type'] in event_type_stoi.keys()]
            else:
                trigger_label_idxs = [trigger_label_stoi[l]
                                    for l in trigger_labels]
                event_type_idxs = [event_type_stoi[e['event_type']] for e in events]
                trigger_list = [(e['trigger']['start'], e['trigger']['end'],
                                event_type_stoi[e['event_type']])
                                for e in events]

            # Relation
            relation_types = get_relation_types(entities, relations,
                                               entity_id_map,
                                               self.test,
                                               relation_type_stoi,
                                               directional=self.relation_directional,
                                               symmetric=self.symmetric_relations)
            relation_type_idxs = [[relation_type_stoi[l] for l in ls]
                                 for ls in relation_types]
            if self.relation_mask_self:
                for i in range(len(relation_type_idxs)):
                    relation_type_idxs[i][i] = -100
            relation_list = get_relation_list(entities, relations,
                                             entity_id_map, relation_type_stoi, self.test,
                                             directional=self.relation_directional,
                                             symmetric=self.symmetric_relations)
            #relation_type_idxs = []
            #relation_list = []

            # Argument role
            role_types = get_role_types(entities, events, entity_id_map, role_type_stoi, self.test)
            role_type_idxs = [[role_type_stoi[l] for l in ls]
                              for ls in role_types]
            role_list = get_role_list(entities, events,
                                      entity_id_map, role_type_stoi, self.test)

            # Graph
            graph = Graph(
                entities=entity_list,
                triggers=trigger_list,
                relations=relation_list,
                roles=role_list,
                mentions=mention_list,
                vocabs=vocabs,
            )
            
            instance = Instance(
                doc_id=doc_id,
                wnd_id=wnd_id,
                sent_id=sent_id,
                tokens=tokens,
                pieces=pieces,
                piece_idxs=piece_idxs,
                token_lens=token_lens,
                attention_mask=attn_mask,
                entity_label_idxs=entity_label_idxs,
                trigger_label_idxs=trigger_label_idxs,
                entity_type_idxs=entity_type_idxs,
                event_type_idxs=event_type_idxs,
                relation_type_idxs=relation_type_idxs,
                mention_type_idxs=mention_type_idxs,
                role_type_idxs=role_type_idxs,
                graph=graph,
                entity_num=len(entities),
                trigger_num=len(events),
            )
            data.append(instance)
        self.data = data

    def collate_fn(self, batch):
        batch_piece_idxs = []
        batch_tokens = []
        batch_entity_labels, batch_trigger_labels = [], []
        batch_entity_types, batch_event_types = [], []
        batch_relation_types, batch_role_types = [], []
        batch_mention_types = []
        batch_graphs = []
        batch_token_lens = []
        batch_attention_masks = []

        sent_ids = [inst.sent_id for inst in batch]
        token_nums = [len(inst.tokens) for inst in batch]
        max_token_num = max(token_nums)

        max_entity_num = max([inst.entity_num for inst in batch] + [1])
        max_trigger_num = max([inst.trigger_num for inst in batch] + [1])
        
        doc_ids = [inst.doc_id for inst in batch]
        wnd_ids = [inst.wnd_id for inst in batch]

        for inst in batch:
            token_num = len(inst.tokens)
            batch_piece_idxs.append(inst.piece_idxs)
            batch_attention_masks.append(inst.attention_mask)
            batch_token_lens.append(inst.token_lens)
            batch_graphs.append(inst.graph)
            batch_tokens.append(inst.tokens)
            # for identification
            batch_entity_labels.append(inst.entity_label_idxs +
                                       [0] * (max_token_num - token_num))
            batch_trigger_labels.append(inst.trigger_label_idxs +
                                        [0] * (max_token_num - token_num))
            # for classification
            batch_entity_types.extend(inst.entity_type_idxs +
                                      [-100] * (max_entity_num - inst.entity_num))
            batch_event_types.extend(inst.event_type_idxs +
                                     [-100] * (max_trigger_num - inst.trigger_num))
            batch_mention_types.extend(inst.mention_type_idxs +
                                       [-100] * (max_entity_num - inst.entity_num))
            for l in inst.relation_type_idxs:
                batch_relation_types.extend(
                    l + [-100] * (max_entity_num - inst.entity_num))
            batch_relation_types.extend(
                [-100] * max_entity_num * (max_entity_num - inst.entity_num))
            for l in inst.role_type_idxs:
                batch_role_types.extend(
                    l + [-100] * (max_entity_num - inst.entity_num))
            batch_role_types.extend(
                [-100] * max_entity_num * (max_trigger_num - inst.trigger_num))

        if self.gpu:
            batch_piece_idxs = torch.cuda.LongTensor(batch_piece_idxs)
            batch_attention_masks = torch.cuda.FloatTensor(
                batch_attention_masks)

            batch_entity_labels = torch.cuda.LongTensor(batch_entity_labels)
            batch_trigger_labels = torch.cuda.LongTensor(batch_trigger_labels)
            batch_entity_types = torch.cuda.LongTensor(batch_entity_types)
            batch_mention_types = torch.cuda.LongTensor(batch_mention_types)
            batch_event_types = torch.cuda.LongTensor(batch_event_types)
            batch_relation_types = torch.cuda.LongTensor(batch_relation_types)
            batch_role_types = torch.cuda.LongTensor(batch_role_types)

            token_nums = torch.cuda.LongTensor(token_nums)
        else:
            batch_piece_idxs = torch.LongTensor(batch_piece_idxs)
            batch_attention_masks = torch.FloatTensor(batch_attention_masks)

            batch_entity_labels = torch.LongTensor(batch_entity_labels)
            batch_trigger_labels = torch.LongTensor(batch_trigger_labels)
            batch_entity_types = torch.LongTensor(batch_entity_types)
            batch_mention_types = torch.LongTensor(batch_mention_types)
            batch_event_types = torch.LongTensor(batch_event_types)
            batch_relation_types = torch.LongTensor(batch_relation_types)
            batch_role_types = torch.LongTensor(batch_role_types)

            token_nums = torch.LongTensor(token_nums)

        return Batch(
            doc_ids=doc_ids,
            wnd_ids=wnd_ids,
            sent_ids=sent_ids,
            tokens=[inst.tokens for inst in batch],
            piece_idxs=batch_piece_idxs,
            token_lens=batch_token_lens,
            attention_masks=batch_attention_masks,
            entity_label_idxs=batch_entity_labels,
            trigger_label_idxs=batch_trigger_labels,
            entity_type_idxs=batch_entity_types,
            mention_type_idxs=batch_mention_types,
            event_type_idxs=batch_event_types,
            relation_type_idxs=batch_relation_types,
            role_type_idxs=batch_role_types,
            graphs=batch_graphs,
            token_nums=token_nums,
        )


class IEDatasetEval(object):
    def __init__(self, path, max_length=200, gpu=False, input_format='txt',
                 language='english'):
        self.path = path
        self.gpu = gpu
        self.max_length = max_length
        self.data = []
        self.doc_id = None
        self.ori_sent_num = 0
        self.input_format = input_format
        self.language = language
        self.load_data()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def load_data(self):
        """Load data from file"""
        if self.input_format == 'txt':
            doc_tokens, doc_id = read_txt(self.path, language=self.language)
        elif self.input_format == 'ltf':
            doc_tokens, doc_id = read_ltf(self.path)
        elif self.input_format == 'json':
            doc_tokens, doc_id = read_json(self.path)
        elif self.input_format == 'json_single':
            doc_tokens, doc_id = read_json_single(self.path)
        else:
            raise ValueError('Unknown input format: {}'.format(self.input_format))
        self.doc_id = doc_id
        self.data = doc_tokens
        self.ori_sent_num = len(doc_tokens)

    def numberize(self, tokenizer):
        data = []
        for i, (sent_id, sent_tokens) in enumerate(self.data):
            tokens = []
            token_ids = []
            pieces = []
            token_lens = []
            for token_text, start_char, end_char in sent_tokens:
                token_id = '{}:{}-{}'.format(self.doc_id, start_char, end_char)
                token_pieces = [p for p in tokenizer.tokenize(token_text) if p]
                if len(token_pieces) == 0:
                    continue
                tokens.append(token_text)
                pieces.extend(token_pieces)
                token_lens.append(len(token_pieces))
                token_ids.append(token_id)

            # skip overlength sentences
            if len(pieces) > self.max_length - 2:
                continue
            # skip empty sentences
            if len(pieces) == 0:
                continue

            # pad word pieces with special tokens
            piece_idxs = tokenizer.encode(pieces,
                                          add_special_tokens=True,
                                          max_length=self.max_length,
                                          truncation=True)
            pad_num = self.max_length - len(piece_idxs)
            attn_mask = [1] * len(piece_idxs) + [0] * pad_num
            piece_idxs = piece_idxs + [0] * pad_num

            instance = InstanceLdcEval(
                # sent_id='{}-{}'.format(self.doc_id, i),
                sent_id=sent_id,
                tokens=tokens,
                token_ids=token_ids,
                pieces=pieces,
                piece_idxs=piece_idxs,
                token_lens=token_lens,
                attention_mask=attn_mask
            )
            data.append(instance)
        self.data = data

    def collate_fn(self, batch):
        batch_piece_idxs = []
        batch_tokens = []
        batch_token_lens = []
        batch_attention_masks = []
        batch_sent_ids = []
        batch_token_ids = []
        batch_token_nums = []

        for inst in batch:
            token_num = len(inst.tokens)
            batch_piece_idxs.append(inst.piece_idxs)
            batch_attention_masks.append(inst.attention_mask)
            batch_token_lens.append(inst.token_lens)
            batch_tokens.append(inst.tokens)
            batch_sent_ids.append(inst.sent_id)
            batch_token_ids.append(inst.token_ids)
            batch_token_nums.append(len(inst.tokens))

        if self.gpu:
            batch_piece_idxs = torch.cuda.LongTensor(batch_piece_idxs)
            batch_attention_masks = torch.cuda.FloatTensor(
                batch_attention_masks)
            batch_token_nums = torch.cuda.LongTensor(batch_token_nums)
        else:
            batch_piece_idxs = torch.LongTensor(batch_piece_idxs)
            batch_attention_masks = torch.FloatTensor(
                batch_attention_masks)
            batch_token_nums = torch.LongTensor(batch_token_nums)

        return BatchLdcEval(sent_ids=batch_sent_ids,
                            token_ids=batch_token_ids,
                            tokens=batch_tokens,
                            piece_idxs=batch_piece_idxs,
                            token_lens=batch_token_lens,
                            attention_masks=batch_attention_masks,
                            token_nums=batch_token_nums)
