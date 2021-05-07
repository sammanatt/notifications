from twilio.rest import Client
import os

# Load environment file, assign variables
from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
twilio_phone_number = os.environ["twilio_phone_number"]
recipient_phone_number = os.environ["recipient_phone_number"]


# your account sid and auth token from twilio.com/console
client = Client(account_sid, auth_token)

message = client.messages.create(
    media_url="https://i.ytimg.com/vi/U_JbTHp6uzI/maxresdefault.jpg",
    body="Why isn't that an API?",
    from_=twilio_phone_number,
    to=recipient_phone_number
)

print(message.sid)