from twilio.rest import Client


def sendMessage(body):
    account_sid = "" #Twillio sid.
    auth_token = "" #Twilio authorization token.
    fromNumber = "" #Twilio purchased phone number. 
    toNumber = "" #your phone number.

    client = Client(account_sid, auth_token)

    message = client.messages.create(

        body = body,
        from_ = fromNumber,
        to = toNumber

    )
    print("text message sent")
