

from twilio.rest import Client
import config

client = Client(config.accountSID_twilio, config.authToken_twilio)


client.messages.create(from_=config.sendNum,
                       to=config.myNum,
                       body='Your code has finished running!')