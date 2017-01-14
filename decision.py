def next(hopeline_id, answer):
    if hopeline_id == 0:
        return {
            'id': 1,
            'message': 'What\'s your name?'
        }
    elif hopeline_id == 1:
        return {
            'id': 2,
            'message': 'Hello, %s!' % answer
        }
    else:
        print(hopeline_id)
        hopeline_id += 1
        return {
            'id': hopeline_id,
            'message': 'new state: %s' % hopeline_id
        }
