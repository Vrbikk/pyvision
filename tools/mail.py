import smtplib
import time
from constants import constants

def send_mail(nvr_list):
	fromaddr = constants.EMAIL
	toaddrs  = constants.EMAIL
	msg = "REPORT: \n"

	for nvr in nvr_list:
		msg += str(nvr) + "\n"
		msg += nvr.get_information() + "\n"

	message = 'Subject: %s\n\n%s' % ("Pyvison report", msg)

	username = constants.EMAIL
	password = constants.EMAIL_PASSWORD

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, message)
	server.quit()
	
