import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
username = "nguyenvanchien9499@gmail.com"
password = "happyKBTG??44"

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(username, password)


def message(subject="Python Notification", text=""):
    # build message contents
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    return msg


def send_email(receiver, title, msg):
    try:
        msg_content = message(title, msg)
        smtp.sendmail(username, receiver, msg_content.as_string())
        return True
    except Exception as e:
        print(f"Fail to send email to {receiver}")
        print(e)
        return False
