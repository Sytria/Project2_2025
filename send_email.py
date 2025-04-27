import smtplib
from email.message import EmailMessage

from_email_addr ="2209984936@qq.com"
from_email_pass ="yjckbhwatwdyeadj"
to_email_addr ="3901966032@qq.com"

msg = EmailMessage()

body ="Hello from Raspberry Pi"
msg.set_content(body)

msg['From'] = from_email_addr
msg['To'] = to_email_addr
msg['Subject'] = 'TEST EMAIL'

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.send_message(msg)

print('Email set')

server.quit()
