import decision
from datetime import datetime


def handle(answer, number, hopeline_state_id, hopeline_timestamp):
    if answer.strip().lower() == 'reset':
        hopeline_state_id = 0
    else:
        hopeline_state_id = hopeline_state_id

    print('-------------')
    print(datetime.now())
    print('%s\t|\t%s\t|\t%s' % (number, hopeline_state_id, answer))
    print('-------------')

    difference = datetime.now() - hopeline_timestamp

    if (difference.total_seconds() > 300):
        hopeline_state_id = 0

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
