

'''
python3 status.py "structs/scan/_status/static/STATUS_1.py"
'''

import cyte._ensure.eq as equality


def PATH ():
	import pathlib
	from os.path import dirname, join, normpath
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	return normpath (join (THIS_FOLDER, "structs.json"))

def CHECK_1 ():
	INCLUDES = "VITAMIN B1"

	def FOR_EACH (STRUCT):
		STRUCT_NAMES = STRUCT ["names"]
			
		for STRUCT_NAME in STRUCT_NAMES:
			STRUCT_NAME = STRUCT_NAME.upper ()
		
			if (STRUCT_NAME == INCLUDES.upper ()):
				return True

		return False

	import cyte.structs.DB.access as access
	import cyte.structs.scan as STRUCT_scan
	structs = STRUCT_scan.START (
		structs_DB = access.DB (PATH ()),
		FOR_EACH = FOR_EACH
	)
	
	print ("structs:", structs)

	equality.check (len (structs), 1)
	equality.check (structs[0]["region"], 20)

	return;
	
	
CHECKS = {
	"check 1": CHECK_1
}