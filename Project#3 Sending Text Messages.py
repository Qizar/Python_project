from twilio.rest import Client

Account_sid = "ACf1ebdb3f0b7d1d8b6f9c5b9daff132c8"
Auth_token = "00d9672af167fbf501f851d70f2a5e88"

client = Client(Account_sid,Auth_token)

message = client.messages.create(
    body = "My name is afzaal",
    to = "+917702993904",
    from_ = "+114172655607")

print(message.sid)
