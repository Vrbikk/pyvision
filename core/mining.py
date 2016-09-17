import xml.etree.ElementTree as ET
import logging, requests, base64
from constants import constants

logger = logging.getLogger("mining")
logging.getLogger("requests").setLevel(logging.WARNING)

def make_url(nvr, path=""):
	return "http://" + nvr.ip + ":" + str(nvr.port) + path	

def get_response(nvr, url):
	try:
		response = requests.get(url, auth=(constants.USER, constants.USER_PASSWORD))

		if response.status_code != 200:
			return None

		#getting rid of some shits
		return str(response.content).replace("\\n", "").replace("b\'", "").replace("\'", "")

	except Exception as e:
		return None

def is_alive(nvr):
	try:
		r = requests.get(make_url(nvr))
	except Exception:
		return "OFFLINE"	

	if r.status_code == 200:
		return "ONLINE"
	else:
		return "OFFLINE"	

# returns list of text values
def get_values(xml, tag): #fix issuewith not valid xml or other bullshit
	values = []

	root = ET.fromstring(xml)
	namespace = root.tag.split('}')[0].strip('{')
	for item in root.findall(".//{" + namespace + "}" + tag):
		values.append(item.text)
	return values	

def get_device_status(nvr):
	logger.info("Retrieving device status of: {}".format(nvr))
	status = is_alive(nvr)
	logger.info("Device is {}: {}".format(status, nvr))	
	return status

def get_device_uptime(nvr):
	logger.info("Retrieving uptime of: {}".format(nvr))
	url = make_url(nvr, constants.STATUS_PATH)
	response = get_response(nvr, url)
	uptime = get_values(response, constants.STATUS_UPTIME)	
	return "{0:.2f} dys of uptime".format(int(uptime[0])/60/60/24)