from email.mime.multipart import MIMEMultipart
# mime - Multipurpose Internet Mail Extension
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template

template = Template(Path("templates.html").read_text())

message = MIMEMultipart()
message["from"] = "Sushrut Patil"
message["to"] = "sareen279@gmail.com"
message["subject"] = "3 baje aa khelnaeko"
body = template.substitute({"name":"Sushrut"})
message.attach(MIMEText(body,"html"))
# message.attach(MIMEText("Sending Through Python","plain"))
message.attach(MIMEImage(Path("image_name").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # tls is Transport Layer Security
    smtp.login("email", "password")
    smtp.send_message(message)
    print("Sent...")
