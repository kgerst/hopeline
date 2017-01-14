from flask import Flask, request, redirect, session
import twilio.twiml
import decision


# The session object makes use of a secret key.
SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

callers = {
    "+19524848117": "Kim"
}


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    answer = request.values['Body']
    hopeline_state_id = session.get('hopeline_state_id', 0)
    resp = twilio.twiml.Response()
    next = decision.next(hopeline_state_id, answer)
    resp.message(next['message'])
    session['hopeline_state_id'] = next['id']
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
