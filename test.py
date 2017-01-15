import decision

hopeline_id = 0

while True:
    s = input('--> ')
    result = decision.next(hopeline_id, s)
    hopeline_id = result['id']
    print('%s:\t%s' % (result['id'], result['message']))
