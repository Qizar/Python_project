# twilio is external package
# To download in windpows open cmd and type the commands pip install twilio
# Go to official website of twilio and sign up
# After signing up, you will get your Account sid, authorization token and twilio phone number
from twilio.rest import Client

Account_sid = "ACf1ebdb3f0b7d1d8b6f9c5b9daff132c8"
Auth_token = "00d9672af167fbf501f851d70f2a5e88"

client = Client(Account_sid,Auth_token)

message = client.messages.create(
    body = "My name is afzaal",
    to = "+917702993904", #  replace with your registered phone number
    from_ = "+114172655607") # replace with your twilio phone number

print(message.sid)
