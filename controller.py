import decision
from datetime import datetime


def handle(answer, number, hopeline_state_id, hopeline_timestamp):
    print('answer\t\t\ttype: %s\t\t\tvalue: %s' % (answer.__class__, answer))
    print('number\t\t\ttype: %s\t\t\tvalue: %s' % (number.__class__, number))
    print('hopeline_state_id\ttype: %s\t\t\tvalue: %s' %
          (hopeline_state_id.__class__, hopeline_state_id))
    print('hopeline_timestamp\ttype: %s\tvalue: %s' %
          (hopeline_timestamp.__class__, hopeline_timestamp))

    if answer.strip().lower() == 'reset':
        hopeline_state_id = 0
    else:
        hopeline_state_id = hopeline_state_id

    print('-------------')
    print(datetime.now())
    print('%s\t|\t%s\t|\t%s' % (number, hopeline_state_id, answer))
    print('-------------')

    try:
        difference = datetime.now() - hopeline_timestamp
        print('difference: %s' % difference)
    except:
        print('difference failed')

    # difference = datetime.now() - datetime.strptime(hopeline_timestamp, '%Y-%m-%d %H:%M:%S.%f')

    # if (difference.total_seconds() > 300):
    # hopeline_state_id = 0

    try:
        next = decision.next(hopeline_state_id, answer.strip().lower())
    except:
        next = decision.next(0, answer.strip())

    return {
        'hopeline_state_id': next['id'],
        'hopeline_timestamp': datetime.now(),
        'hopeline_message': next['message']
    }


if __name__ == "__main__":
    handle('answer', 'my number', 0, str(datetime.now()))
