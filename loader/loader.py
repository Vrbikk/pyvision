import os, sys, csv, logging
from classes import nvr

logger = logging.getLogger("loader")

number_of_parameters = 4

def load(path= os.path.dirname(os.path.realpath(__file__)).replace("/loader", "") + "/data/devices.csv"):
	
	try:	
		with open(path) as csvfile:
			reader = csv.reader(csvfile, delimiter=';')
			reader = filter(lambda x: len(x) == number_of_parameters, reader)
			nvr_list = []

			for row in reader:
				try:
					nvr_list.append(nvr.Nvr(row[0], row[1], row[2], row[3]))
				except ValueError as e:
					logger.error("Failed to initialize Nvr class because: [{}] on line {}".format(e, row))	

			if nvr_list:
				logger.info("Loaded {} devices".format(len(nvr_list)))
				for device in nvr_list:
					logger.debug(device)
				return nvr_list			
			else:
				logger.error("No devices loaded stopping")	
				sys.exit(1)
					
	except FileNotFoundError:
		logger.error("File not found {} stopping".format(path))
		sys.exit(1)

