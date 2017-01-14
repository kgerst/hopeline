def next(hopeline_id, answer):
    if (hopeline_id == 0):
        return "What's your name?"
    else:
        return "Hello, %s!" % answer
