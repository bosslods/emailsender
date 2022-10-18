from email import contentmanager
from multiprocessing import context
import smtplib, ssl
from email.message import EmailMessage, Message


port = 465
sender = "kouse@kraziemail.ml"
password = "YqhR1XOayRb0A6Ne"

message = EmailMessage()
message['From'] = sender
message['Subject'] = input('Enter the subject: ')
message['To'] = input("Enter the receiver: ")
message.set_content(input("Enter your message: "))

context = ssl.create_default_context()

print("Sending...")
with smtplib.SMTP_SSL('mail.smtp2go.com', port, context=context) as server:
    server.login(sender, password)
    server.send_message(message)
    
print("Sent...!")