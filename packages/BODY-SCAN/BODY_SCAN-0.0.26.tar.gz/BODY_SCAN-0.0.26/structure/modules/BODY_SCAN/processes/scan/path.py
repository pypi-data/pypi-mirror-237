
'''
	import BODY_SCAN.PROCESSES.SCAN.PATH as SCAN_PATH
	SCAN_PATH.FIND ()
'''
'''
	This returns the path of the "scan" process.
'''


import pathlib
from os.path import dirname, join, normpath

path = "python3_scan_process"

def FIND ():
	this_folder = pathlib.Path (__file__).parent.resolve ()
	return normpath (join (this_folder, path))