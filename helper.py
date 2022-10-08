"""Module for any helper methods
"""
import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from email.mime.text import MIMEText


load_dotenv()


def mifflin_st_jeor(age, weight, height, gender):
    """calculate the bmr using mifflin equation [standard for now]"""
    if gender == "m":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    return int(bmr)


def send_message(message, sender, receiver):
    with smtplib.SMTP(
        os.environ['SMTP_HOST'], os.environ['SMTP_PORT']
    ) as server:
        server.login(os.environ['SMTP_USER'], os.environ['SMTP_PASS'])
        server.sendmail(sender, receiver, message.as_string())


def make_message(email, bmr):
    sender = os.environ['DEVEMAIL']
    message = MIMEText(f"Your BMR is: {bmr}")
    message["Subject"] = "Your BMR is here!"
    message["From"] = sender
    message["To"] = email

    send_message(message, sender, email)
