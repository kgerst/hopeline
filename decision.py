import options

def next(hopeline_id, answer): 
    options_dict = {
        ("ask feeling", 'yes'): options.suggest_911(),
        ("ask feeling", 'no'): options.ask_if_they_reached_out(),
        ("suggest 911", 'yes'): options.suggest_skills(),
        ("suggest 911", 'no'): options.goodbye(),        
        ("ask if they reached out", 'yes'): options.suggest_skills(),
        ("ask if they reached out", 'no'): options.ask_willingness(),
        ("ask willingness", 'yes'): options.ask_type_of_contact(),
        ("ask willingness", 'no'): options.suggest_skills(),
        ("ask type of contact", 'professional'): options.give_resources(),
        ("ask type of contact", 'personal'): options.suggest_how_to_start_convo(),
        ("give resources", 'yes'): options.suggest_skills(),
        ("give resources", 'no'): options.goodbye(),
        ("suggest how to start a convo", 'yes'): options.suggest_skills(),
        ("suggest how to start a convo", 'no'): options.goodbye(),
        ("skills general", 'yes'): options.hygiene(),
        ("skills general", 'no'): options.goodbye(),
        ("skill 1", 'yes'): options.watch_a_short_video(),
        ("skill 1", 'no'): options.goodbye(),
        ("skill 2", 'yes'): options.meditate(),
        ("skill 2", 'no'): options.goodbye(),
        ("skill 3", 'yes'): options.walk(),
        ("skill 3", 'no'): options.goodbye(),
        ("skill 4", 'yes'): options.suggest_skills(), # this is gross logic
        ("skill 4", 'no'): options.goodbye(),        
    }
    if hopeline_id == 0 or answer == 'reset':
        return options.ask_feeling()
    else:
        return options_dict[(hopeline_id, answer)]

