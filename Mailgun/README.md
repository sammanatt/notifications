# Mailgun
Leverage a set of powerful APIs to send, receive and track emails. 

At the time of writing this, you can sign up for an account and send up to 5,000 emails per month for the first three months. After that, pricing is pretty darn reasonable ($0.80 per month for 1,000 emails).

---
## Setup
1. Sign up for an account at: https://signup.mailgun.com/new/signup
2. Clone this repo
3. Run `pip install -r requirements.txt`
3. Create a `.env` file with variables to setup the following variables:
* mailgun_apikey=YOUR_API_KEY
* domain=YOUR_DOMAIN
* from_address=SENDER_EMAIL_ADDRESS
* to_address=RECIPIENT_EMAIL_ADDRESS

>Note: You can of course use a list to supply multiple recipients in the same email job.