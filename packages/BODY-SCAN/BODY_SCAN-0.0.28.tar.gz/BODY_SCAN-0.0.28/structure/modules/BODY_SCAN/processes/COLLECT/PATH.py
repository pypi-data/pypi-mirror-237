



'''
	import BODY_SCAN.PROCESSES.COLLECT.PATH as COLLECT_PATH
	COLLECT_PATH.FIND ()
'''
import pathlib
from os.path import dirname, join, normpath

def FIND ():
	return normpath (join (pathlib.Path (__file__).parent.resolve (), "START.PROC.PY"))