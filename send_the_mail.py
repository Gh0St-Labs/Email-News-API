import ssl
import smtplib
import os
def email(the_message):
    host = "smtp.gmail.com"
    port = 465

    gmail = "syondukeabraham@gmail.com"
    password = os.getenv("PWD")

    reciever = ['syondukeabraham@gmail.com', 'neilbestin@gmail.com']
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(gmail, password)
        server.sendmail(gmail, reciever, msg=the_message)
