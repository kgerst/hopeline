import os

from flask import Flask, request, session
import twilio.twiml

import controller

# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route("/help", methods=['GET', 'POST'])
def help():
    number = request.values['From']
    answer = request.values['Body']
    hopeline_state_id = session.get('hopeline_state_id', 0)
    hopeline_timestamp = session.get('hopeline_timestamp', '1970-01-01 00:00:00.000')

    result = controller.handle(answer, number, hopeline_state_id, hopeline_timestamp)

    resp = twilio.twiml.Response()
    resp.message(result['hopeline_message'])

    session['hopeline_state_id'] = result['hopeline_state_id']
    session['hopeline_timestamp'] = result['hopeline_timestamp']

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
