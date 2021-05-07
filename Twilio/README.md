# Twilio Messaging
Easily send messages (sms, mms, WhatsApp, et al) via an API. To get started (no credit card required!) sign up for an account at: https://www.twilio.com/try-twilio

At the time of writing this, completing missions in [TwilioQuest](https://www.twilio.com/quest) can earn you credits towards messaging fees. Heck, you can even [plant trees IRL](https://www.twilio.com/blog/explore-the-cloud-and-plant-trees-in-twilioquest-for-earth-day-2021)!!

---
## Setup
1. Sign up for an account at: https://www.twilio.com/try-twilio 
2. Clone this repo
3. Run `pip install -r requirements.txt`
3. Create a `.env` file with variables to setup the following variables:
    * account_sid='YOUR_ID'
    * auth_token='YOUR_AUTH_TOKEN'
    * recipient_phone_number=RECIPIENT_NUMBER
    * twilio_phone_number=TWILIO_NUMBER
