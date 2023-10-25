
'''
	import pathlib
	from os.path import dirname, join, normpath
	
	this_folder = pathlib.Path (__file__).parent.resolve ()
	search = normpath (join (this_folder, "../.."))

	import BODY_SCAN
	BODY_SCAN.START (
		GLOB = search + '/**/*STATUS.py'
	)
'''

import glob

import BODY_SCAN.aggregate as aggregate
import BODY_SCAN.processes.scan as scan

def START (
	GLOB = "",
	
	RELATIVE_PATH = False,
	
	MODULE_PATHS = [],
	
	SIMULTANEOUS = False,
	
	print_alarms = True,
	
	RECORDS = 0	
):
	FINDS = glob.glob (GLOB, recursive = True)
		
	if (RECORDS >= 1):
		print ()
		print ("SEARCHING FOR GLOB:")
		print ("	", GLOB)
		print ()
	
	if (RECORDS >= 1):
		print ()
		print ("	FINDS:", FINDS)
		print ("	FINDS COUNT:", len (FINDS))
		print ();
	
	def START_SIMULTANEOUSLY ():
		OUTPUT = []
	
		def FN (PATH):
			[ STATUS ] = scan.start (		
				PATH = PATH,
				MODULE_PATHS = MODULE_PATHS,
				RELATIVE_PATH = RELATIVE_PATH,
				RECORDS = RECORDS
			)
		
			return STATUS;
		
		from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
		with ThreadPoolExecutor () as executor:
			RETURNS = executor.map (
				FN, 
				FINDS
			)
			
			executor.shutdown (wait = True)
			
			for RETURN in RETURNS:
				OUTPUT.append (RETURN)
				
			
		return OUTPUT;
	
	
	def START_SEQUENTIALLY ():
		'''
			STARTS MULTIPLE SCANS, SEQUENTIALLY...
		'''
		PATH_STATUSES = []
		for PATH in FINDS:	
			[ STATUS ] = scan.start (		
				PATH = PATH,
				MODULE_PATHS = MODULE_PATHS,
				RELATIVE_PATH = RELATIVE_PATH,
				RECORDS = RECORDS
			)
			
			PATH_STATUSES.append (STATUS)
			
		return PATH_STATUSES;


	if (SIMULTANEOUS == True):
		PATH_STATUSES = START_SIMULTANEOUSLY ()
	else:
		PATH_STATUSES = START_SEQUENTIALLY ()

	STATUS = aggregate.start (
		PATH_STATUSES
	)


	import json
	print ("STATUS:", json.dumps (STATUS, indent = 4))
	
	def alarm_printer (paths):
		alarms = []
	
		for path in paths:
			#print ("path:", path)
			#print ()

			if (path ["parsed"] == False):
				alarms.append (path)

			if ("CHECKS" not in path):
				continue;
		
		
			checks = path ["CHECKS"]
		
			this_path = path ["PATH"]
			unsuccessful = []
			
			for check in checks:
				if (check ["PASSED"] == False):
					unsuccessful.append (check)
			
			if (len (unsuccessful) >= 1):
				alarms.append ({
					"path": this_path,
					"checks": unsuccessful
				})
				
		print ("alarms:", json.dumps (alarms, indent = 4))
		
	if (print_alarms):
		alarm_printer (STATUS ["PATHS"])
		
	print ("STATS:", json.dumps (STATUS ["STATS"], indent = 4))	
		
	return {
		"STATUS": STATUS
	}
	
