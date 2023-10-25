

'''
	python3 STATUS.py "structs/scan/net/status_cryo/STATUS_1.py"
'''

import cyte.structs.DB.access as access
import cyte.structs.scan.TREES as TREES

import json

def PATH ():
	import pathlib
	from os.path import dirname, join, normpath
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	return normpath (join (THIS_FOLDER, "structs.json"))

def CHECK_1 ():
	#STRUCT_DB = access.DB (PATH (), sort_keys = True)
	STRUCT_DB = access.DB ()

	import cyte.structs.scan.net as net_build
	struct_net = net_build.start (STRUCT_DB)
	

	
	
CHECKS = {
	"CHECK 1": CHECK_1
}