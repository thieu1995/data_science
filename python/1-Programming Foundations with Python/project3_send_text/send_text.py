from twilio import rest

account_sid = "AC1d3186b3cd92cb94e66a0731df9f6da8" # Your Account SID from www.twilio.com/console
auth_token  = "a46e268e7d206c26158963fbcd2917d9"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hi! I'm Angie. I'm come from US. I'm your big fan since we first met. Now I'm in HaNoi. Can I see you?",
    to="+841677397048",    # Replace with your phone number
    from_="+13077635373") # Replace with your Twilio number

print(message.sid)
