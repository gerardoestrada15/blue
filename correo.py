!/usr/bin/python
import smtplib
import ssl
from email.message import EmailMessage

subject= "Email from Igo&see"
body= "Personal fuera del area de trabajo"
sender_email= "amphenolacademia2@gmail.com"
receiver_email="gerardoestrada15@gmail.com"
password="academialean"

message=EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]=subject
message.set_content(body)

context=ssl.create_default_context()
print("Enviando Email")
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string())
print("Mensaje enviado")    