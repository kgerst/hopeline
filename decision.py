import options

def next(hopeline_id, answer): 
    options_dict = {
        (1, 'yes'): options.suggest_911(),
        (1, 'no'): options.ask_to_reach_out(),
        (3, 'yes'): options.suggest_skills(),
        (3, 'no'): options.ask_willingness(),
        (4, 'yes'): options.ask_type_of_contact(),
        (4, 'no'): options.suggest_skills(),
        (5, 'professional'): options.give_resources(),
        (5, 'personal'): options.suggest_how_to_start_convo()
    }
    if hopeline_id == 0 or answer == 'reset':
        return options.ask_feeling()
    else:
        return options_dict[(hopeline_id, answer)]

