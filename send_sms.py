# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC47d78139ed0314e4cf17f58df8509d56"
auth_token = "0f5ae91b8fc6ca1150a0cd5a2c3c1eeb"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+19524848117", from_="+16122497336",
                                     body="Hi this is me!")