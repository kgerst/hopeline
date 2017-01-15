from datetime import datetime
import os

from flask import Flask, request, session
import twilio.twiml

import decision

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route("/help", methods=['GET', 'POST'])
def help():
    answer = request.values['Body']
    hopeline_state_id = session.get('hopeline_state_id', 0)
    hopeline_timestamp = session.get('hopeline_timestamp', '1970-01-01 00:00:00.000')
    previous = datetime.strptime(hopeline_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    difference = datetime.now() - previous

    if (difference.total_seconds() > 300):
        hopeline_state_id = 0

    next = decision.next(hopeline_state_id, answer)

    resp = twilio.twiml.Response()
    resp.message(next['message'])

    session['hopeline_state_id'] = next['id']
    session['hopeline_timestamp'] = str(datetime.now())

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
