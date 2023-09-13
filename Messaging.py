from twilio.rest import Client


def sendMessage(body):
    account_sid = "" #Twillio sid.
    auth_token = "" #Twilio authorization token.
    from_phone_number = "from_phone_number"
    to_phone_number = "to_phone_number"

    client = Client(account_sid, auth_token)

    message = client.messages.create(

        body = body,
        from_ = from_phone_number,
        to = to_phone_number

    )
    print("text message sent")
