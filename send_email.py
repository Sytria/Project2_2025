import smtplib
from email.message import EmailMessage

from_email_addr ="202483890028@nuist.edu.cn"
from_email_pass ="qldm0525"
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
