import os
from twilio.rest import Client

# Load environment file, assign variables
from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
recipient_phone_number = os.environ["recipient_phone_number"]
twilio_phone_number = os.environ["twilio_phone_number"]

# Your Account Sid and Auth Token from twilio.com/console
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=twilio_phone_number,
    body='hello world',
    to=recipient_phone_number
)

print(message.sid)
