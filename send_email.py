import smtplib, ssl
import os

def send_email(message):
    port = 465
    host = "smtp.gmail.com"

    username = "ibrohimovmuhammad2020@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "ibrohimovmuhammad2020@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
