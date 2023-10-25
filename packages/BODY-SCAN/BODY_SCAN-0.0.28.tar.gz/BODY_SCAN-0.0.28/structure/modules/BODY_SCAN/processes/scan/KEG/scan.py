



def scan_file (path):
	with open (path, mode = 'r') as selector:
		return selector.read ()

def build_scan_string (path):
	contents = scan_file (path)
	contents += '''
		
try:
	______BODY_SCAN ["CHECKS"] = CHECKS;	
	______BODY_SCAN ["CHECKS FOUND"] = True;
except Exception as E:
	print (E)
	______BODY_SCAN ["CHECKS FOUND"] = False;
		'''

	return contents


import BODY_SCAN.functions.exceptions as bs_exceptions

import json
import time
from time import sleep, perf_counter as pc


def scan (FIND):
	# PATH = {}
	
	FINDINGS = []
	STATS = {
		"PASSES": 0,
		"ALARMS": 0
	}

	PATH_E = ""

	try:
		CONTENTS = build_scan_string (FIND)
		
		______BODY_SCAN = {}
		exec (
			CONTENTS, 
			{ 
				'______BODY_SCAN': ______BODY_SCAN,
				'__file__': FIND
			}
		)
		

		if (______BODY_SCAN ["CHECKS FOUND"] == False):
			return {
				"EMPTY": True,
				"parsed": True
			}

		
		CHECKS = ______BODY_SCAN ['CHECKS']		

		
		for CHECK in CHECKS:
			try:
				TIME_START = pc ()
				CHECKS [ CHECK ] ()
				TIME_END = pc ()
				TIME_ELAPSED = TIME_END - TIME_START

				FINDINGS.append ({
					"CHECK": CHECK,
					"PASSED": True,
					"ELAPSED": [ TIME_ELAPSED, "SECONDS" ]
				})
				
				STATS ["PASSES"] += 1
				
			except Exception as E:				
				FINDINGS.append ({
					"CHECK": CHECK,
					"PASSED": False,
					"EXCEPTION": repr (E),
					"EXCEPTION TRACE": bs_exceptions.find_trace (E)
				})
				
				STATS ["ALARMS"] += 1
		
		
		return {
			"empty": False,
			"parsed": True,
						
			"STATS": STATS,			
			"CHECKS": FINDINGS
		}
		
	except Exception as E:		
		PATH_E = E;

	return {
		"parsed": False,
		"ALARM": "An exception occurred while scanning the path.",
		"EXCEPTION": repr (PATH_E),
		"EXCEPTION TRACE": bs_exceptions.find_trace (PATH_E)
	}