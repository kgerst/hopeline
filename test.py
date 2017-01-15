import controller
from datetime import datetime


number = '###'
hopeline_state_id = 0
hopeline_timestamp = datetime.now()

while True:
    answer = input('--> ')
    result = controller.handle(answer, number, hopeline_state_id, hopeline_timestamp)
    hopeline_state_id = result['hopeline_state_id']
    hopeline_timestamp = result['hopeline_timestamp']
    print(result['hopeline_message'])
