import logging
from loader import *
from classes import nvr
from xml.dom import minidom
from tools import mail
import requests
import xml.etree.ElementTree as ET
from core import mining

logger = logging.getLogger("core")

def scan():	
	logger.info("Starting scan procedure")
	nvr_list = loader.load()

	for i in range(0, len(nvr_list)):
		nvr_list[i].status = mining.get_device_status(nvr_list[i])
		
		if nvr_list[i].status == "ONLINE":
			nvr_list[i].uptime = mining.get_device_uptime(nvr_list[i])

	logger.info('Finished scan procedure')	

	logger.info("Sending mail report")
		
	mail.send_mail(nvr_list)

	

