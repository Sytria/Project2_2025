import smtplib
import RPi.GPIO as GPIO
import time
from email.message import EmailMessage

channel = 4
GPIO.setmode(GPIO.BCM) 
GPIO.setup(channel, GPIO.IN)


from_email_addr = "2209984986@qq.com"
from_email_pass = "yjckbhwatwdyeadj"
to_email_addr = "3901966032@qq.com"

lastValue = -1
lastTime = 0

def callback(channel):
	global lastValue
	if GPIO.input(channel):
		print ("Water detected!")
		lastValue = 1
	else:
		print ("Water not detected!")
		lastValue = 0
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(channel, callback)

def send_email(subject, body):
	server = smtplib.SMTP('smtp.qq.com', 25)
	server.starttls()
	server.login(from_email_addr, from_email_pass)

	msg = EmailMessage()
	msg.set_content(body)
	msg['Subject'] = subject
	msg['From'] = from_email_addr
	msg['To'] = to_email_addr

	server.send_message(msg)
	server.quit()
	print ("email sent")


def main():
	global lastTime, lastValue
	while True:
		current_time = time.localtime()
		current_hour = current_time.tm_hour + 8
		print ("Current time hour: ", current_hour)

		if current_hour != lastTime:
			print ("Time to send the first email of the day")
			send_email("test email", "Hello from Raspberry Pi")
			lastTime = current_hour

		differenve = current_hour - lastValue
		if difference > 3:
			print ("Time difference > 3, time to send an email")
			send_email("Water needed. ", "Please water youur plant")
			lastValue = current_hour

		else:
			print("Time difference < 4, do not email")

		time.sleep(60)

if __name__ == "__main__":
	main()
