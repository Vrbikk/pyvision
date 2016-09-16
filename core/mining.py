import xml.etree.ElementTree as ET
import logging, requests, base64
from constants import constants

logger = logging.getLogger("mining")
logging.getLogger("requests").setLevel(logging.WARNING)

def make_url(nvr, path):
	return "http://" + nvr.ip + ":" + str(nvr.port) + path	

def get_response(nvr, url):
	try:
		response = requests.get(url, auth=(constants.USER, constants.USER_PASSWORD))

		if response.status_code != 200:
			logger.error("Device is OFFLINE: {}".format(nvr))
			return "OFFLINE"

		logger.info("Device is ONLINE: {}".format(nvr))	
		#getting rid of some shits
		return str(response.content).replace("\\n", "").replace("b\'", "").replace("\'", "")

	except Exception as e:
		logger.error("Request to {} FAILED with error: {}".format(nvr, e))
		return "OFFLINE"

# returns list of text values
def get_values(xml, tag):
	values = []

	root = ET.fromstring(xml)
	namespace = root.tag.split('}')[0].strip('{')
	for item in root.findall(".//{" + namespace + "}" + tag):
		values.append(item.text)
	return values	

def get_device_status(nvr):
	logger.info("Retrieving device status of: {}".format(nvr))

	url = make_url(nvr, constants.STATUS_PATH)

	response = get_response(nvr, url)

	uptime = get_values(response, constants.STATUS_UPTIME)	

	return "ONLINE {0:.2f} days uptime".format(int(uptime[0])/60/60/24)
