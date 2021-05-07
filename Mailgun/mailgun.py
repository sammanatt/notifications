import os
import requests

# Load environment file, assign variables
from dotenv import load_dotenv
load_dotenv()

mailgun_apikey = os.environ["mailgun_apikey"]
domain = os.environ["domain"]
from_address = os.environ["from_address"]
to_address = os.environ["to_address"]


def send_simple_message():
    message = requests.post(
        "https://api.mailgun.net/v3/"+ domain + "/messages",
        auth=("api", mailgun_apikey),
        data={"from": from_address,
              "to": to_address, 
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
    print(f"message: {message.text}\n"
        f"status:{message.status_code}" )



send_simple_message()

