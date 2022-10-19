from email import message
from multiprocessing import context
from re import S
import smtplib, ssl
from email.message import EmailMessage
from decoder import Z, decoded_creds

print("Simple Python Email Sender")

port = 465
SENDER_USERNAME= Z.decod3_user()
SENDER_PASSWORD = Z.decod3_pass()

message = EmailMessage()
message['From'] = SENDER_USERNAME
message['Subject'] = input("Enter the subject: ")
message['To'] = input("To: ")
message.set_content(input("Your Message: "))

context = ssl.create_default_context()

print("Sending... Please wait")

with smtplib.SMTP_SSL('mail.smtp2go.com', port, context=context) as mailer:
    mailer.login(SENDER_USERNAME, SENDER_PASSWORD)
    mailer.send_message(message)
    
print("Email succesfully sent")


