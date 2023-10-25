

'''
	This is the scan process starter.
'''

'''
	steps:
		1. 	A scan process is started.
			1. the scan process has a flask (a.k.a. keg or reservoir) server built in.
		
		2. 	A request is sent to the scan process to run checks found
			in a path.
		
		3. 	The returns (status and stats) of the scan process are returned.
'''

from BOTANIST.PORTS.FIND_AN_OPEN_PORT import FIND_AN_OPEN_PORT
from BOTANIST.PROCESSES.START_MULTIPLE import START_MULTIPLE as START_MULTIPLE_PROCESSES

import BODY_SCAN.processes.scan.path as SCAN_PATH
	
import sys
import json
def ATTEMPT_TAP_KEG (
	MODULE_PATHS
):
	PORT = FIND_AN_OPEN_PORT ()
	SCAN_PROCESS_PATH = SCAN_PATH.FIND ()

	details = json.dumps ({ "MODULE_PATHS": sys.path })
	string = f'''python3 { SCAN_PROCESS_PATH } KEG OPEN --port { PORT } --details \'{ details }\' '''

	PROCS = START_MULTIPLE_PROCESSES (
		PROCESSES = [{
			"STRING": string,
			"CWD": None
		}]
	)

	return [ PORT, PROCS ]

def start (
	PATH,
	MODULE_PATHS = [],
	RELATIVE_PATH = False,
	RECORDS = 0
):
	[ PORT, PROCS ] = ATTEMPT_TAP_KEG (
		MODULE_PATHS
	)
	
	import time
	time.sleep (0.5)
	
	REQUEST_ADDRESS = f'http://127.0.0.1:{ PORT }'
	
	import json
	import requests
	r = requests.put (
		REQUEST_ADDRESS, 
		data = json.dumps ({ 
			"FINDS": [ PATH ],
			"MODULE PATHS": MODULE_PATHS,
			"RELATIVE PATH": RELATIVE_PATH
		})
	)
	
	def FORMAT_RESPONSE (TEXT):
		import json
		return json.loads (TEXT)
	
	STATUS = FORMAT_RESPONSE (r.text)

	if (RECORDS >= 1):
		print ()
		print ("REQUEST ADDRESS :", REQUEST_ADDRESS)
		print ("REQUEST STATUS  :", r.status_code)
		print ("REQUEST TEXT  :", json.dumps (STATUS, indent = 4))
		print ()


	EXIT 			= PROCS ["EXIT"]
	PROCESSES 		= PROCS ["PROCESSES"]
	
	return [ STATUS ]