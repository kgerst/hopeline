import decision

hopeline_id = 0

while True:
    s = input('--> ')
    next = decision.next(hopeline_id, s)
    hopeline_id = next['id']
    print('%s:\t%s' % (next['id'], next['message']))
