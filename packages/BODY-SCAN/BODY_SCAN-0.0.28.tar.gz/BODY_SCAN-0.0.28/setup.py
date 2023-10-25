
#
#	https://setuptools.pypa.io/en/latest/userguide/quickstart.html
#
#	https://github.com/pypa/sampleproject/blob/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.py
#
from setuptools import setup, find_packages

VERSION = "0.0.28"
NAME = 'BODY_SCAN'
INSTALL_REQUIRES = [ 'BOTANIST', 'click', 'flask' ]

def scan_description ():
	DESCRIPTION = ''
	try:
		with open ('module.txt') as f:
			DESCRIPTION = f.read ()
		print (DESCRIPTION)
	except Exception as E:
		pass;
		
	return DESCRIPTION;

setup (
    name = NAME,
    version = VERSION,
    install_requires = INSTALL_REQUIRES,	
	
	package_dir = { 
		NAME: 'structure/modules/BODY_SCAN'
	},
	
	#
	#
	include_package_data = True,
	package_data = {
		"": [ "*.PY" ]
    },
	
	
	license = "LL",
	
	project_urls = {
		"GitLab": "https://gitlab.com/reptilian_climates/body_scan.git"
	},
	
	long_description = scan_description (),
	#long_description_content_type = "text/markdown",
	long_description_content_type = "text/plain"
)