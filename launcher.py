#!/usr/bin/python3

from core import core
from constants import constants
import sys, time, logging, os


if __name__ == "__main__":

	logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(name)s - %(message)s',
	filename= os.path.dirname(os.path.realpath(__file__)) +'/log.log', level=logging.DEBUG, datefmt='%d-%m-%Y %H:%M:%S')
	#logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(name)s - %(message)s',
	#level=logging.DEBUG, datefmt='%d-%m-%Y %H:%M:%S')

	if len(sys.argv) == 6:

		constants.EMAIL = sys.argv[2]
		constants.EMAIL_PASSWORD = sys.argv[3]
		constants.USER = sys.argv[4]
		constants.USER_PASSWORD = sys.argv[5]

		if 'test' == sys.argv[1]:
			core.scan()
		elif 'scan' == sys.argv[1]:
			core.scan()
		elif 'restart' == sys.argv[1]:
			core.scan()
		else:
			print("Unknown command")
			sys.exit(2)
		sys.exit(0)
	else:
		print("usage: {} scan|test|restart".format(sys.argv[0]))
		sys.exit(2)