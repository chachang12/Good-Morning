from twilio.rest import Client


def sendMessage(body):
    account_sid = "AC955273c9ad6df3ada3b8f403d72a0c41"
    auth_token = "4d0533c9223825046ceff27dbe9ed5a5"
    from_phone_number = "from_phone_number"
    to_phone_number = "to_phone_number"

    client = Client(account_sid, auth_token)

    message = client.messages.create(

        body = body,
        from_ = from_phone_number,
        to = to_phone_number

    )
    print("text message sent")