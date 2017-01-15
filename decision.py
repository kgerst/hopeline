import options

def next(hopeline_id, answer): 
    options_dict = {
        (1, 'Yes'): options.suggest_911(),
        (1, 'No'): options.ask_to_reach_out(),
        (3, 'Yes'): options.suggest_skills(),
        (3, 'No'): options.ask_willingness(),
        (4, 'Yes'): options.ask_type_of_contact(),
        (4, 'No'): options.suggest_skills(),
        (5, 'Professional'): options.give_resources(),
        (5, 'Personal'): options.suggest_how_to_start_convo()
    }
    if hopeline_id == 0:
        return options.ask_feeling()
    else:
        return options_dict[(hopeline_id, answer)]

