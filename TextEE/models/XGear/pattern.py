patterns = {
    "ace05-en": {
        "Business:Declare-Bankruptcy": ["Org"], 
        "Business:End-Org": ["Org", "Place"], 
        "Business:Merge-Org": ["Org"], 
        "Business:Start-Org": ["Agent", "Org", "Place"], 
        "Conflict:Attack": ["Attacker", "Target", "Instrument", "Place", "Agent"], 
        "Conflict:Demonstrate": ["Entity", "Place"], 
        "Contact:Meet": ["Entity", "Place"], 
        "Contact:Phone-Write": ["Entity", "Place"], 
        "Justice:Acquit": ["Defendant", "Adjudicator"], 
        "Justice:Appeal": ["Plaintiff", "Place", "Adjudicator"], 
        "Justice:Arrest-Jail": ["Person", "Agent", "Place"], 
        "Justice:Charge-Indict": ["Defendant", "Prosecutor", "Place", "Adjudicator"], 
        "Justice:Convict": ["Defendant", "Place", "Adjudicator"], 
        "Justice:Execute": ["Person", "Agent", "Place"], 
        "Justice:Extradite": ["Person", "Destination", "Origin", "Agent"], 
        "Justice:Fine": ["Entity", "Place", "Adjudicator"], 
        "Justice:Pardon": ["Defendant", "Adjudicator"], 
        "Justice:Release-Parole": ["Person", "Entity", "Place"], 
        "Justice:Sentence": ["Defendant", "Place", "Adjudicator"], 
        "Justice:Sue": ["Defendant", "Plaintiff", "Place", "Adjudicator"], 
        "Justice:Trial-Hearing": ["Defendant", "Prosecutor", "Place", "Adjudicator"], 
        "Life:Be-Born": ["Person", "Place"], 
        "Life:Die": ["Agent", "Victim", "Instrument", "Place"], 
        "Life:Divorce": ["Person", "Place"], 
        "Life:Injure": ["Agent", "Victim", "Instrument", "Place"], 
        "Life:Marry": ["Person", "Place"], 
        "Movement:Transport": ["Artifact",  "Destination", "Origin", "Vehicle", "Agent", "Place"], 
        "Personnel:Elect": ["Person", "Entity", "Place"], 
        "Personnel:End-Position": ["Person", "Entity", "Place"], 
        "Personnel:Nominate": ["Person", "Agent"], 
        "Personnel:Start-Position": ["Person", "Entity", "Place"], 
        "Transaction:Transfer-Money": ["Giver", "Recipient", "Place", "Beneficiary"], 
        "Transaction:Transfer-Ownership": ["Buyer", "Artifact", "Seller", "Place", "Beneficiary"], 
    }, 
    "richere-en": {
        "Business:Start-Org": ["Agent", "Org", "Place"], 
        "Business:Merge-Org": ["Org"], 
        "Business:End-Org": ["Org", "Place"], 
        "Business:Declare-Bankruptcy": ["Org"], 
        "Conflict:Attack": ["Attacker", "Target", "Instrument", "Place", "Agent"], 
        "Conflict:Demonstrate": ["Entity", "Place"], 
        "Contact:Meet": ["Entity", "Place"], 
        "Contact:Correspondence": ["Entity", "Place"], 
        "Contact:Broadcast": ["Entity", "Audience", "Place"], 
        "Contact:Contact": ["Entity", "Place"], 
        "Justice:Arrest-Jail": ["Person", "Agent", "Place"], 
        "Justice:Release-Parole": ["Person", "Agent", "Place"], 
        "Justice:Trial-Hearing": ["Defendant", "Prosecutor", "Place", "Adjudicator"], 
        "Justice:Charge-Indict": ["Defendant", "Prosecutor", "Place", "Adjudicator"], 
        "Justice:Sue": ["Defendant", "Plaintiff", "Place", "Adjudicator"], 
        "Justice:Convict": ["Defendant", "Place", "Adjudicator"], 
        "Justice:Appeal": ["Defendant", "Place", "Adjudicator", "Prosecutor"], 
        "Justice:Sentence": ["Defendant", "Place", "Adjudicator"], 
        "Justice:Fine": ["Entity", "Place", "Adjudicator"], 
        "Justice:Execute": ["Person", "Agent", "Place"], 
        "Justice:Extradite": ["Person", "Destination", "Origin", "Agent"], 
        "Justice:Acquit": ["Defendant", "Adjudicator", "Place"], 
        "Justice:Pardon": ["Defendant", "Adjudicator", "Place"], 
        "Life:Be-Born": ["Person", "Place"], 
        "Life:Marry": ["Person", "Place"], 
        "Life:Divorce": ["Person", "Place"], 
        "Life:Injure": ["Agent", "Victim", "Instrument", "Place"], 
        "Life:Die": ["Agent", "Victim", "Instrument", "Place"], 
        "Movement:Transport-Person": ["Person", "Destination", "Origin", "Instrument", "Agent"], 
        "Movement:Transport-Artifact": ["Artifact", "Destination", "Origin", "Agent"], 
        "Manufacture:Artifact": ["Artifact", "Agent", "Place"], 
        "Personnel:Start-Position": ["Person", "Entity", "Place"], 
        "Personnel:End-Position": ["Person", "Entity", "Place"], 
        "Personnel:Nominate": ["Person", "Agent", "Place"], 
        "Personnel:Elect": ["Person", "Agent", "Place"], 
        "Transaction:Transfer-Ownership": ["Thing", "Giver", "Recipient", "Place", "Beneficiary"], 
        "Transaction:Transfer-Money": ["Giver", "Recipient", "Place", "Beneficiary"], 
        "Transaction:Transaction": ["Giver", "Recipient", "Place", "Beneficiary"], 
    },
    "m2e2": {
        "Conflict:Attack": ["Attacker", "Target", "Instrument", "Place"], 
        "Conflict:Demonstrate": ["Entity", "Place", "Police"], 
        "Contact:Meet": ["Entity", "Place"], 
        "Contact:Phone-Write": ["Entity", "Place"],         
        "Justice:Arrest-Jail": ["Person", "Agent", "Place"],
        "Life:Die": ["Agent", "Victim", "Instrument", "Place"], 
        "Movement:Transport": ["Artifact",  "Destination", "Origin", "Vehicle", "Agent"], 
        "Transaction:Transfer-Money": ["Giver", "Recipient"], 
    }, 
    "geneva": {
        "Achieve": ["Agent", "Goal", "Means"],
        "Action": ["Act", "Agent", "Domain", "Manner"],
        "Adducing": ["Medium", "Role", "Speaker", "Specified_entity"],
        "Agree_or_refuse_to_act": ["Proposed_action", "Speaker"],
        "Arranging": ["Agent", "Configuration", "Location", "Theme"],
        "Arrest": ["Authorities", "Charges", "Offense", "Suspect"],
        "Arriving": ["Goal", "Means", "Path", "Place", "Purpose", "Source", "Theme"],
        "Assistance": ["Benefited_party", "Focal_entity", "Goal", "Helper", "Means"],
        "Attack": ["Assailant", "Means", "Victim", "Weapon"],
        "Bearing_arms": ["Protagonist", "Weapon"],
        "Becoming": ["Entity", "Final_category", "Final_quality"],
        "Becoming_a_member": ["Group", "New_member"],
        "Bodily_harm": ["Agent", "Body_part", "Cause", "Instrument", "Victim"],
        "Bringing": ["Agent", "Area", "Carrier", "Goal", "Source", "Theme"],
        "Building": ["Agent", "Components", "Created_entity", "Place"],
        "Catastrophe": ["Cause", "Patient", "Place", "Undesirable_event"],
        "Causation": ["Actor", "Affected", "Cause", "Effect", "Means"],
        "Cause_change_of_position_on_a_scale": ["Agent", "Attribute", "Cause", "Difference", "Item", "Value_1", "Value_2"],
        "Cause_to_amalgamate": ["Agent", "Part_1", "Part_2", "Parts", "Whole"],
        "Cause_to_make_progress": ["Agent", "Project"],
        "Change": ["Agent", "Attribute", "Cause", "Entity", "Final_category", "Final_value", "Initial_category"],
        "Change_of_leadership": ["Body", "New_leader", "Old_leader", "Old_order", "Role", "Selector"],
        "Check": ["Inspector", "Means", "Unconfirmed_content"],
        "Choosing": ["Chosen", "Cognizer", "Possibilities"],
        "Collaboration": ["Partners", "Undertaking"],
        "Come_together": ["Configuration", "Individuals", "Place"],
        "Coming_to_be": ["Components", "Entity", "Place", "Time"],
        "Coming_to_believe": ["Cognizer", "Content", "Means"],
        "Commerce_buy": ["Buyer", "Goods", "Seller"],
        "Commerce_pay": ["Buyer", "Goods", "Money", "Seller"],
        "Commerce_sell": ["Buyer", "Goods", "Money", "Seller"],
        "Commitment": ["Addressee", "Message", "Speaker"],
        "Committing_crime": ["Crime", "Instrument", "Perpetrator"],
        "Communication": ["Addressee", "Interlocutors", "Message", "Speaker", "Topic", "Trigger"],
        "Competition": ["Competition", "Participants", "Venue"],
        "Confronting_problem": ["Activity", "Experiencer"],
        "Connect": ["Figures", "Ground"],
        "Conquering": ["Conqueror", "Means", "Theme"],
        "Containing": ["Container", "Contents"],
        "Control": ["Controlling_variable", "Dependent_variable"],
        "Convincing": ["Addressee", "Content", "Speaker", "Topic"],
        "Cost": ["Asset", "Goods", "Intended_event", "Payer", "Rate"],
        "Create_artwork": ["Activity", "Culture"],
        "Creating": ["Cause", "Created_entity", "Creator"],
        "Criminal_investigation": ["Incident", "Investigator", "Suspect"],
        "Cure": ["Affliction", "Medication", "Patient", "Treatment"],
        "Damaging": ["Agent", "Cause", "Patient"],
        "Death": ["Deceased"],
        "Deciding": ["Cognizer", "Decision"],
        "Defending": ["Assailant", "Defender", "Instrument", "Victim"],
        "Departing": ["Goal", "Path", "Source", "Traveller"],
        "Destroying": ["Cause", "Destroyer", "Means", "Patient"],
        "Dispersal": ["Agent", "Cause", "Goal_area", "Individuals"],
        "Earnings_and_losses": ["Earner", "Earnings", "Goods"],
        "Education_teaching": ["Course", "Fact", "Role", "Skill", "Student", "Subject", "Teacher"],
        "Emergency": ["Place", "Undesirable_event"],
        "Employment": ["Employee", "Employer", "Field", "Place_of_employment", "Position", "Task", "Type"],
        "Emptying": ["Agent", "Cause", "Source", "Theme"],
        "Exchange": ["Exchanger_1", "Exchanger_2", "Exchangers", "Theme_1", "Theme_2", "Themes"],
        "Expansion": ["Agent", "Dimension", "Initial_size", "Item", "Result_size"],
        "Filling": ["Agent", "Cause", "Goal", "Theme"],
        "GetReady": ["Activity", "Protagonist"],
        "Getting": ["Means", "Recipient", "Source", "Theme"],
        "Giving": ["Offerer", "Recipient", "Theme"],
        "Hindering": ["Action", "Hindrance", "Protagonist"],
        "Hold": ["Entity", "Manipulator"],
        "Hostile_encounter": ["Instrument", "Issue", "Purpose", "Side_1", "Side_2", "Sides"],
        "Influence": ["Action", "Agent", "Behavior", "Cognizer", "Product", "Situation"],
        "Ingestion": ["Ingestibles", "Ingestor"],
        "Judgment_communication": ["Addressee", "Communicator", "Evaluee", "Medium", "Reason", "Topic"],
        "Killing": ["Cause", "Instrument", "Killer", "Means", "Victim"],
        "Know": ["Cognizer", "Evidence", "Instrument", "Means", "Phenomenon", "Topic"],
        "Labeling": ["Entity", "Label", "Speaker"],
        "Legality": ["Action", "Object"],
        "Manufacturing": ["Factory", "Instrument", "Producer", "Product", "Resource"],
        "Motion": ["Agent", "Area", "Cause", "Distance", "Goal", "Means", "Path", "Source", "Speed", "Theme"],
        "Motion_directional": ["Area", "Direction", "Goal", "Path", "Source", "Theme"],
        "Openness": ["Barrier", "Theme", "Useful_location"],
        "Participation": ["Event", "Participants"],
        "Perception_active": ["Direction", "Perceiver_agentive", "Phenomenon"],
        "Placing": ["Agent", "Cause", "Location", "Theme"],
        "Practice": ["Action", "Agent", "Occasion"],
        "Presence": ["Circumstances", "Duration", "Entity", "Inherent_purpose", "Place", "Time"],
        "Preventing_or_letting": ["Agent", "Event", "Means", "Potential_hindrance"],
        "Process_end": ["Agent", "Cause", "Final_subevent", "Process", "State", "Time"],
        "Process_start": ["Agent", "Event", "Initial_subevent", "Time"],
        "Protest": ["Addressee", "Arguer", "Content"],
        "Quarreling": ["Arguer2", "Arguers", "Issue"],
        "Ratification": ["Proposal", "Ratifier"],
        "Receiving": ["Donor", "Recipient", "Theme"],
        "Recovering": ["Agent", "Entity", "Means"],
        "Removing": ["Agent", "Cause", "Goal", "Source", "Theme"],
        "Request": ["Addressee", "Medium", "Message", "Speaker"],
        "Research": ["Field", "Researcher", "Topic"],
        "Resolve_problem": ["Agent", "Cause", "Means", "Problem"],
        "Response": ["Agent", "Responding_entity", "Response", "Trigger"],
        "Reveal_secret": ["Addressee", "Information", "Speaker", "Topic"],
        "Revenge": ["Avenger", "Injured_party", "Injury", "Offender", "Punishment"],
        "Rite": ["Member", "Object", "Type"],
        "Scrutiny": ["Cognizer", "Ground", "Instrument", "Phenomenon", "Unwanted_entity"],
        "Self_motion": ["Direction", "Distance", "Goal", "Path", "Self_mover", "Source"],
        "Sending": ["Goal", "Means", "Recipient", "Sender", "Source", "Theme", "Transferors", "Vehicle"],
        "Sign_agreement": ["Agreement", "Signatory"],
        "Social_event": ["Attendees", "Beneficiary", "Host", "Occasion", "Social_event"],
        "Statement": ["Addressee", "Medium", "Message", "Speaker"],
        "Supply": ["Imposed_purpose", "Recipient", "Supplier", "Theme"],
        "Supporting": ["Supported", "Supporter"],
        "Telling": ["Addressee", "Message", "Speaker"],
        "Terrorism": ["Act", "Instrument", "Terrorist", "Victim"],
        "Testing": ["Circumstances", "Means", "Product", "Result", "Tested_property", "Tester"],
        "Theft": ["Goods", "Instrument", "Means", "Perpetrator", "Source", "Victim"],
        "Traveling": ["Area", "Distance", "Entity", "Goal", "Means", "Path", "Purpose", "Traveler"],
        "Using": ["Agent", "Instrument", "Means", "Purpose"],
        "Wearing": ["Body_location", "Clothing", "Wearer"],
        "Writing": ["Addressee", "Author", "Instrument", "Text"],
    },
    "maven": {
        "Achieve": [],
        "Action": [],
        "Adducing": [],
        "Agree_or_refuse_to_act": [],
        "Aiming": [],
        "Arranging": [],
        "Arrest": [],
        "Arriving": [],
        "Assistance": [],
        "Attack": [],
        "Award": [],
        "Bearing_arms": [],
        "Becoming": [],
        "Becoming_a_member": [],
        "Being_in_operation": [],
        "Besieging": [],
        "Bodily_harm": [],
        "Body_movement": [],
        "Breathing": [],
        "Bringing": [],
        "Building": [],
        "Carry_goods": [],
        "Catastrophe": [],
        "Causation": [],
        "Cause_change_of_position_on_a_scale": [],
        "Cause_change_of_strength": [],
        "Cause_to_amalgamate": [],
        "Cause_to_be_included": [],
        "Cause_to_make_progress": [],
        "Change": [],
        "Change_event_time": [],
        "Change_of_leadership": [],
        "Change_sentiment": [],
        "Change_tool": [],
        "Check": [],
        "Choosing": [],
        "Collaboration": [],
        "Come_together": [],
        "Coming_to_be": [],
        "Coming_to_believe": [],
        "Commerce_buy": [],
        "Commerce_pay": [],
        "Commerce_sell": [],
        "Commitment": [],
        "Committing_crime": [],
        "Communication": [],
        "Competition": [],
        "Confronting_problem": [],
        "Connect": [],
        "Conquering": [],
        "Containing": [],
        "Control": [],
        "Convincing": [],
        "Cost": [],
        "Create_artwork": [],
        "Creating": [],
        "Criminal_investigation": [],
        "Cure": [],
        "Damaging": [],
        "Death": [],
        "Deciding": [],
        "Defending": [],
        "Departing": [],
        "Destroying": [],
        "Dispersal": [],
        "Earnings_and_losses": [],
        "Education_teaching": [],
        "Emergency": [],
        "Employment": [],
        "Emptying": [],
        "Escaping": [],
        "Exchange": [],
        "Expansion": [],
        "Expend_resource": [],
        "Expressing_publicly": [],
        "Extradition": [],
        "Filling": [],
        "Forming_relationships": [],
        "GetReady": [],
        "Getting": [],
        "GiveUp": [],
        "Giving": [],
        "Having_or_lacking_access": [],
        "Hiding_objects": [],
        "Hindering": [],
        "Hold": [],
        "Hostile_encounter": [],
        "Imposing_obligation": [],
        "Incident": [],
        "Influence": [],
        "Ingestion": [],
        "Institutionalization": [],
        "Judgment_communication": [],
        "Justifying": [],
        "Kidnapping": [],
        "Killing": [],
        "Know": [],
        "Labeling": [],
        "Legal_rulings": [],
        "Legality": [],
        "Lighting": [],
        "Limiting": [],
        "Manufacturing": [],
        "Military_operation": [],
        "Motion": [],
        "Motion_directional": [],
        "Name_conferral": [],
        "Openness": [],
        "Participation": [],
        "Patrolling": [],
        "Perception_active": [],
        "Placing": [],
        "Practice": [],
        "Presence": [],
        "Preserving": [],
        "Preventing_or_letting": [],
        "Prison": [],
        "Process_end": [],
        "Process_start": [],
        "Protest": [],
        "Publishing": [],
        "Quarreling": [],
        "Ratification": [],
        "Receiving": [],
        "Recording": [],
        "Recovering": [],
        "Reforming_a_system": [],
        "Releasing": [],
        "Removing": [],
        "Renting": [],
        "Reporting": [],
        "Request": [],
        "Rescuing": [],
        "Research": [],
        "Resolve_problem": [],
        "Response": [],
        "Reveal_secret": [],
        "Revenge": [],
        "Rewards_and_punishments": [],
        "Risk": [],
        "Rite": [],
        "Robbery": [],
        "Scouring": [],
        "Scrutiny": [],
        "Self_motion": [],
        "Sending": [],
        "Sign_agreement": [],
        "Social_event": [],
        "Statement": [],
        "Submitting_documents": [],
        "Supply": [],
        "Supporting": [],
        "Surrendering": [],
        "Surrounding": [],
        "Suspicion": [],
        "Telling": [],
        "Temporary_stay": [],
        "Terrorism": [],
        "Testing": [],
        "Theft": [],
        "Traveling": [],
        "Use_firearm": [],
        "Using": [],
        "Violence": [],
        "Vocalizations": [],
        "Warning": [],
        "Wearing": [],
        "Writing": [],
    },
    "mee-en": {
        "Business_START-ORG": ["Agent", "Organization", "Place", "Time"], 
        "Conflict_Attack": ["Attacker", "Instrument", "Place", "Target", "Time"], 
        "Conflict_Demonstrate": ["Entity", "Place", "Time"], 
        "Contact_Meet": ["Entity", "Place", "Time"], 
        "Contact_Phone-Write": ["Entity", "Time"], 
        "Justice_Arrest-Jail": ["Agent", "Crime", "Person", "Place", "Time"], 
        "Life_Be-Born": ["Person", "Place", "Time"], 
        "Life_Die": ["Agent", "Instrument", "Place", "Time", "Victim"], 
        "Life_Divorce": ["Person", "Place", "Time"], 
        "Life_Injure": ["Agent", "Instrument", "Place", "Time", "Victim"], 
        "Life_Marry": ["Person", "Place", "Time"], 
        "Movement_Transport": ["Agent", "Artifact",  "Destination", "Origin", "Time", "Vehicle"], 
        "Personnel_End-Position": ["Entity", "Person", "Place", "Position", "Time"], 
        "Personnel_Start-Position": ["Entity", "Person", "Place", "Position", "Time"], 
        "Transaction_Transfer-Money": ["Beneficiary", "Giver", "Money", "Place", "Recipient", "Time"], 
        "Transaction_Transfer-Ownership": ["Artifact", "Beneficiary", "Buyer", "Money", "Place", "Price", "Seller", "Time"], 
    }, 
    "rams": {
        "artifactexistence.damagedestroy.damage": ["artifact", "damager", "instrument", "place"],
        "artifactexistence.damagedestroy.destroy": ["artifact", "destroyer", "instrument", "place"],
        "artifactexistence.damagedestroy.n/a": ["artifact", "damagerdestroyer", "instrument", "place"],
        "conflict.attack.airstrikemissilestrike": ["attacker", "instrument", "place", "target"],
        "conflict.attack.biologicalchemicalpoisonattack": ["attacker", "instrument", "place", "target"],
        "conflict.attack.bombing": ["attacker", "instrument", "place", "target"],
        "conflict.attack.firearmattack": ["attacker", "instrument", "place", "target"],
        "conflict.attack.hanging": ["attacker", "instrument", "place", "target"],
        "conflict.attack.invade": ["attacker", "instrument", "place", "target"],
        "conflict.attack.n/a": ["attacker", "instrument", "place", "target"],
        "conflict.attack.selfdirectedbattle": ["attacker", "instrument", "place", "target"],
        "conflict.attack.setfire": ["attacker", "instrument", "place", "target"],
        "conflict.attack.stabbing": ["attacker", "instrument", "place", "target"],
        "conflict.attack.stealrobhijack": ["artifact", "attacker", "instrument", "place", "target"],
        "conflict.attack.strangling": ["attacker", "instrument", "place", "target"],
        "conflict.demonstrate.marchprotestpoliticalgathering": ["demonstrator", "place"],
        "conflict.demonstrate.n/a": ["demonstrator", "place"],
        "conflict.yield.n/a": ["place", "recipient", "yielder"],
        "conflict.yield.retreat": ["destination", "origin", "retreater"],
        "conflict.yield.surrender": ["place", "recipient", "surrenderer"],
        "contact.collaborate.correspondence": ["participant", "place"],
        "contact.collaborate.meet": ["participant", "place"],
        "contact.collaborate.n/a": ["participant", "place"],
        "contact.commandorder.broadcast": ["communicator", "place", "recipient"],
        "contact.commandorder.correspondence": ["communicator", "place", "recipient"],
        "contact.commandorder.meet": ["communicator", "place", "recipient"],
        "contact.commandorder.n/a": ["communicator", "place", "recipient"],
        "contact.commitmentpromiseexpressintent.broadcast": ["communicator", "place", "recipient"],
        "contact.commitmentpromiseexpressintent.correspondence": ["communicator", "place", "recipient"],
        "contact.commitmentpromiseexpressintent.meet": ["communicator", "place", "recipient"],
        "contact.commitmentpromiseexpressintent.n/a": ["communicator", "place", "recipient"],
        "contact.discussion.correspondence": ["participant", "place"],
        "contact.discussion.meet": ["participant", "place"],
        "contact.discussion.n/a": ["participant", "place"],
        "contact.funeralvigil.meet": ["deceased", "participant", "place"],
        "contact.funeralvigil.n/a": ["deceased", "participant", "place"],
        "contact.mediastatement.broadcast": ["communicator", "place", "recipient"],
        "contact.mediastatement.n/a": ["communicator", "place", "recipient"],
        "contact.negotiate.correspondence": ["participant", "place"],
        "contact.negotiate.meet": ["participant", "place"],
        "contact.negotiate.n/a": ["participant", "place"],
        "contact.prevarication.broadcast": ["communicator", "place", "recipient"],
        "contact.prevarication.correspondence": ["communicator", "place", "recipient"],
        "contact.prevarication.meet": ["communicator", "place", "recipient"],
        "contact.prevarication.n/a": ["communicator", "place", "recipient"],
        "contact.publicstatementinperson.broadcast": ["communicator", "place", "recipient"],
        "contact.publicstatementinperson.n/a": ["communicator", "place", "recipient"],
        "contact.requestadvise.broadcast": ["communicator", "place", "recipient"],
        "contact.requestadvise.correspondence": ["communicator", "place", "recipient"],
        "contact.requestadvise.meet": ["communicator", "place", "recipient"],
        "contact.requestadvise.n/a": ["communicator", "place", "recipient"],
        "contact.threatencoerce.broadcast": ["communicator", "place", "recipient"],
        "contact.threatencoerce.correspondence": ["communicator", "place", "recipient"],
        "contact.threatencoerce.meet": ["communicator", "place", "recipient"],
        "contact.threatencoerce.n/a": ["communicator", "place", "recipient"],
        "disaster.accidentcrash.accidentcrash": ["crashobject", "driverpassenger", "place", "vehicle"],
        "disaster.fireexplosion.fireexplosion": ["fireexplosionobject", "instrument", "place"],
        "government.agreements.acceptagreementcontractceasefire": ["participant", "place"],
        "government.agreements.n/a": ["participant", "place"],
        "government.agreements.rejectnullifyagreementcontractceasefire": ["otherparticipant", "place", "rejecternullifier"],
        "government.agreements.violateagreement": ["otherparticipant", "place", "violator"],
        "government.formation.mergegpe": ["participant", "place"],
        "government.formation.n/a": ["founder", "gpe", "place"],
        "government.formation.startgpe": ["founder", "gpe", "place"],
        "government.legislate.legislate": ["governmentbody", "law", "place"],
        "government.spy.spy": ["beneficiary", "observedentity", "place", "spy"],
        "government.vote.castvote": ["ballot", "candidate", "place", "result", "voter"],
        "government.vote.n/a": ["ballot", "candidate", "place", "result", "voter"],
        "government.vote.violationspreventvote": ["ballot", "candidate", "place", "preventer", "voter"],
        "inspection.sensoryobserve.inspectpeopleorganization": ["inspectedentity", "inspector", "place"],
        "inspection.sensoryobserve.monitorelection": ["monitor", "monitoredentity", "place"],
        "inspection.sensoryobserve.n/a": ["observedentity", "observer", "place"],
        "inspection.sensoryobserve.physicalinvestigateinspect": ["inspectedentity", "inspector", "place"],
        "justice.arrestjaildetain.arrestjaildetain": ["crime", "detainee", "jailer", "place"],
        "justice.initiatejudicialprocess.chargeindict": ["crime", "defendant", "judgecourt", "place", "prosecutor"],
        "justice.initiatejudicialprocess.n/a": ["crime", "defendant", "judgecourt", "place", "prosecutor"],
        "justice.initiatejudicialprocess.trialhearing": ["crime", "defendant", "judgecourt", "place", "prosecutor"],
        "justice.investigate.investigatecrime": ["crime", "defendant", "investigator", "place"],
        "justice.investigate.n/a": ["defendant", "investigator", "place"],
        "justice.judicialconsequences.convict": ["crime", "defendant", "judgecourt", "place"],
        "justice.judicialconsequences.execute": ["crime", "defendant", "executioner", "place"],
        "justice.judicialconsequences.extradite": ["crime", "defendant", "destination", "extraditer", "origin"],
        "justice.judicialconsequences.n/a": ["crime", "defendant", "judgecourt", "place"],
        "life.die.deathcausedbyviolentevents": ["instrument", "killer", "place", "victim"],
        "life.die.n/a": ["place", "victim"],
        "life.die.nonviolentdeath": ["place", "victim"],
        "life.injure.illnessdegradationhungerthirst": ["place", "victim"],
        "life.injure.illnessdegradationphysical": ["victim"],
        "life.injure.injurycausedbyviolentevents": ["injurer", "instrument", "place", "victim"],
        "life.injure.n/a": ["injurer", "place", "victim"],
        "manufacture.artifact.build": ["artifact", "instrument", "manufacturer", "place"],
        "manufacture.artifact.createintellectualproperty": ["artifact", "instrument", "manufacturer", "place"],
        "manufacture.artifact.createmanufacture": ["artifact", "instrument", "manufacturer", "place"],
        "manufacture.artifact.n/a": ["artifact", "instrument", "manufacturer", "place"],
        "movement.transportartifact.bringcarryunload": ["artifact", "destination", "origin", "transporter", "vehicle"],
        "movement.transportartifact.disperseseparate": ["artifact", "destination", "origin", "transporter", "vehicle"],
        "movement.transportartifact.fall": ["artifact", "destination", "origin"],
        "movement.transportartifact.grantentry": ["artifact", "destination", "origin", "transporter"],
        "movement.transportartifact.hide": ["artifact", "hidingplace", "origin", "transporter", "vehicle"],
        "movement.transportartifact.n/a": ["artifact", "destination", "origin", "transporter", "vehicle"],
        "movement.transportartifact.nonviolentthrowlaunch": ["artifact", "destination", "origin", "transporter", "vehicle"],
        "movement.transportartifact.prevententry": ["artifact", "destination", "origin", "preventer", "transporter"],
        "movement.transportartifact.preventexit": ["artifact", "destination", "origin", "preventer", "transporter"],
        "movement.transportartifact.receiveimport": ["artifact", "destination", "origin", "transporter", "vehicle"],
        "movement.transportartifact.sendsupplyexport": ["artifact", "destination", "origin", "transporter", "vehicle"],
        "movement.transportartifact.smuggleextract": ["artifact", "destination", "origin", "transporter", "vehicle"],
        "movement.transportperson.bringcarryunload": ["destination", "origin", "passenger", "transporter", "vehicle"],
        "movement.transportperson.disperseseparate": ["destination", "origin", "passenger", "transporter", "vehicle"],
        "movement.transportperson.evacuationrescue": ["destination", "origin", "passenger", "transporter", "vehicle"],
        "movement.transportperson.fall": ["destination", "origin", "passenger"],
        "movement.transportperson.grantentryasylum": ["destination", "granter", "origin", "passenger", "transporter"],
        "movement.transportperson.hide": ["hidingplace", "origin", "passenger", "transporter", "vehicle"],
        "movement.transportperson.n/a": ["destination", "origin", "passenger", "transporter", "vehicle"],
        "movement.transportperson.prevententry": ["destination", "origin", "passenger", "preventer", "transporter"],
        "movement.transportperson.preventexit": ["destination", "origin", "passenger", "preventer", "transporter"],
        "movement.transportperson.selfmotion": ["destination", "origin", "transporter"],
        "movement.transportperson.smuggleextract": ["destination", "origin", "passenger", "transporter", "vehicle"],
        "personnel.elect.n/a": ["candidate", "place", "voter"],
        "personnel.elect.winelection": ["candidate", "place", "voter"],
        "personnel.endposition.firinglayoff": ["employee", "place", "placeofemployment"],
        "personnel.endposition.n/a": ["employee", "place", "placeofemployment"],
        "personnel.endposition.quitretire": ["employee", "place", "placeofemployment"],
        "personnel.startposition.hiring": ["employee", "place", "placeofemployment"],
        "personnel.startposition.n/a": ["employee", "place", "placeofemployment"],
        "transaction.transaction.embargosanction": ["artifactmoney", "giver", "place", "preventer", "recipient"],
        "transaction.transaction.giftgrantprovideaid": ["beneficiary", "giver", "place", "recipient"],
        "transaction.transaction.n/a": ["beneficiary", "participant", "place"],
        "transaction.transaction.transfercontrol": ["beneficiary", "giver", "place", "recipient", "territoryorfacility"],
        "transaction.transfermoney.borrowlend": ["beneficiary", "giver", "money", "place", "recipient"],
        "transaction.transfermoney.embargosanction": ["giver", "money", "place", "preventer", "recipient"],
        "transaction.transfermoney.giftgrantprovideaid": ["beneficiary", "giver", "money", "place", "recipient"],
        "transaction.transfermoney.n/a": ["beneficiary", "giver", "money", "place", "recipient"],
        "transaction.transfermoney.payforservice": ["beneficiary", "giver", "money", "place", "recipient"],
        "transaction.transfermoney.purchase": ["beneficiary", "giver", "money", "place", "recipient"],
        "transaction.transferownership.borrowlend": ["artifact", "beneficiary", "giver", "place", "recipient"],
        "transaction.transferownership.embargosanction": ["artifact", "giver", "place", "preventer", "recipient"],
        "transaction.transferownership.giftgrantprovideaid": ["artifact", "beneficiary", "giver", "place", "recipient"],
        "transaction.transferownership.n/a": ["artifact", "beneficiary", "giver", "place", "recipient"],
        "transaction.transferownership.purchase": ["artifact", "beneficiary", "giver", "place", "recipient"],  
    },
    "wikievents": {
        "ArtifactExistence.DamageDestroyDisableDismantle.Damage": ["Artifact", "Damager", "Instrument", "Place"],
        "ArtifactExistence.DamageDestroyDisableDismantle.Destroy": ["Artifact", "Destroyer", "Instrument", "Place"],
        "ArtifactExistence.DamageDestroyDisableDismantle.DisableDefuse": ["Artifact", "Disabler", "Instrument"],
        "ArtifactExistence.DamageDestroyDisableDismantle.Dismantle": ["Artifact", "Components", "Dismantler", "Instrument", "Place"],
        "ArtifactExistence.DamageDestroyDisableDismantle.Unspecified": ["Artifact", "DamagerDestroyer", "Instrument", "Place"],
        "ArtifactExistence.ManufactureAssemble.Unspecified": ["Artifact", "Components", "ManufacturerAssembler", "Place"],
        "Cognitive.IdentifyCategorize.Unspecified": ["IdentifiedObject", "IdentifiedRole", "Identifier", "Place"],
        "Cognitive.Inspection.SensoryObserve": ["Instrument", "ObservedEntity", "Observer", "Place"],
        "Cognitive.Research.Unspecified": ["Place", "Researcher", "Subject"],
        "Cognitive.TeachingTrainingLearning.Unspecified": ["Learner", "TeacherTrainer"],
        "Conflict.Attack.DetonateExplode": ["Attacker", "ExplosiveDevice", "Instrument", "Place", "Target"],
        "Conflict.Attack.Unspecified": ["Attacker", "Instrument", "Place", "Target"],
        "Conflict.Defeat.Unspecified": ["Defeated", "Place", "Victor"],
        "Conflict.Demonstrate.DemonstrateWithViolence": ["Demonstrator", "Regulator"],
        "Conflict.Demonstrate.Unspecified": ["Demonstrator", "Target", "Topic"],
        "Contact.Contact.Broadcast": ["Communicator", "Instrument", "Place", "Recipient", "Topic"],
        "Contact.Contact.Correspondence": ["Participant", "Place", "Topic"],
        "Contact.Contact.Meet": ["Participant", "Place", "Topic"],
        "Contact.Contact.Unspecified": ["Participant", "Place", "Topic"],
        "Contact.RequestCommand.Broadcast": ["Communicator", "Recipient"],
        "Contact.RequestCommand.Correspondence": ["Communicator", "Recipient", "Topic"],
        "Contact.RequestCommand.Meet": ["Communicator", "Recipient"],
        "Contact.RequestCommand.Unspecified": ["Communicator", "Place", "Recipient"],
        "Contact.ThreatenCoerce.Broadcast": ["Communicator", "Recipient"],
        "Contact.ThreatenCoerce.Correspondence": ["Communicator", "Recipient"],
        "Contact.ThreatenCoerce.Unspecified": ["Communicator", "Recipient"],
        "Control.ImpedeInterfereWith.Unspecified": ["Impeder", "Place"],
        "Disaster.Crash.Unspecified": ["CrashObject", "Place", "Vehicle"],
        "Disaster.DiseaseOutbreak.Unspecified": ["Place", "Victim"],
        "GenericCrime.GenericCrime.GenericCrime": ["Perpetrator", "Place", "Victim"],
        "Justice.Acquit.Unspecified": ["Defendant"],
        "Justice.ArrestJailDetain.Unspecified": ["Detainee", "Jailer", "Place"],
        "Justice.ChargeIndict.Unspecified": ["Defendant", "JudgeCourt", "Place", "Prosecutor"],
        "Justice.Convict.Unspecified": ["Defendant", "JudgeCourt"],
        "Justice.InvestigateCrime.Unspecified": ["Defendant", "Investigator", "ObservedEntity", "Observer", "Place"],
        "Justice.ReleaseParole.Unspecified": ["Defendant", "JudgeCourt"],
        "Justice.Sentence.Unspecified": ["Defendant", "JudgeCourt", "Place"],
        "Justice.TrialHearing.Unspecified": ["Defendant", "JudgeCourt", "Place", "Prosecutor"],
        "Life.Die.Unspecified": ["Killer", "Place", "Victim"],
        "Life.Infect.Unspecified": ["Victim"],
        "Life.Injure.Unspecified": ["BodyPart", "Injurer", "Instrument", "Victim"],
        "Medical.Intervention.Unspecified": ["Patient", "Place", "Treater"],
        "Movement.Transportation.Evacuation": ["Destination", "Origin", "PassengerArtifact", "Transporter"],
        "Movement.Transportation.IllegalTransportation": ["Destination", "PassengerArtifact", "Transporter", "Vehicle"],
        "Movement.Transportation.PreventPassage": ["Destination", "Origin", "PassengerArtifact", "Preventer", "Transporter", "Vehicle"],
        "Movement.Transportation.Unspecified": ["Destination", "Origin", "PassengerArtifact", "Transporter", "Vehicle"],
        "Personnel.EndPosition.Unspecified": ["Employee", "PlaceOfEmployment"],
        "Personnel.StartPosition.Unspecified": ["Employee", "Place", "PlaceOfEmployment", "Position"],
        "Transaction.Donation.Unspecified": ["ArtifactMoney", "Giver", "Recipient"],
        "Transaction.ExchangeBuySell.Unspecified": ["AcquiredEntity", "Giver", "PaymentBarter", "Recipient"],
    },
    "phee": {
        "Adverse_event": [
            "Combination_Drug",
            "Effect",
            "Subject",
            "Subject_Age",
            "Subject_Disorder",
            "Subject_Gender",
            "Subject_Population",
            "Subject_Race",
            "Treatment",
            "Treatment_Disorder",
            "Treatment_Dosage",
            "Treatment_Drug",
            "Treatment_Duration",
            "Treatment_Freq",
            "Treatment_Route",
            "Treatment_Time_elapsed"
        ],
        "Potential_therapeutic_event": [
            "Combination_Drug",
            "Effect",
            "Subject",
            "Subject_Age",
            "Subject_Disorder",
            "Subject_Gender",
            "Subject_Population",
            "Subject_Race",
            "Treatment",
            "Treatment_Disorder",
            "Treatment_Dosage",
            "Treatment_Drug",
            "Treatment_Duration",
            "Treatment_Freq",
            "Treatment_Route",
            "Treatment_Time_elapsed"
        ]
    },
    "casie": {
        "Attack:Databreach": [
            "Attack-Pattern",
            "Attacker",
            "Compromised-Data",
            "Damage-Amount",
            "Number-of-Data",
            "Number-of-Victim",
            "Place",
            "Purpose",
            "Time",
            "Tool",
            "Victim"
        ],
        "Attack:Phishing": [
            "Attack-Pattern",
            "Attacker",
            "Damage-Amount",
            "Place",
            "Purpose",
            "Time",
            "Tool",
            "Trusted-Entity",
            "Victim",
        ],
        "Attack:Ransom": [
            "Attack-Pattern",
            "Attacker",
            "Damage-Amount",
            "Payment-Method",
            "Place",
            "Price",
            "Time",
            "Tool",
            "Victim",
        ],
        "Vulnerability-related:DiscoverVulnerability": [
            "CVE",
            "Capabilities",
            "Discoverer",
            "Supported_Platform",
            "Time",
            "Vulnerability",
            "Vulnerable_System",
            "Vulnerable_System_Owner",
            "Vulnerable_System_Version",
        ],
        "Vulnerability-related:PatchVulnerability": [
            "CVE",
            "Issues-Addressed",
            "Patch",
            "Patch-Number",
            "Releaser",
            "Supported_Platform",
            "Time",
            "Vulnerability",
            "Vulnerable_System",
            "Vulnerable_System_Version",
        ],
    },
}
