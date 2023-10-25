




'''
	python3 STATUS.py "structs/sculpt/names/status_cryo/STATUS_1.py"
'''


import cyte.structs.scan.regions.find_next as FIND_NEXT_REGION
import cyte.structs.sculpt.STRUCT.insert as STRUCT_INSERT
import cyte.structs.scan.struct.list as structs_LIST
	

def PATH (ADDRESS):
	import shutil

	import pathlib
	from os.path import dirname, join, normpath
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	
	SOURCE = normpath (join (THIS_FOLDER, "structs.json"))
	DEST = normpath (join (THIS_FOLDER, ADDRESS))
	
	shutil.copyfile (SOURCE, DEST)
	
	return DEST;
	
def DELETE_PATH (ADDRESS):
	import pathlib
	from os.path import dirname, join, normpath
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	DEST = normpath (join (THIS_FOLDER, ADDRESS))
	
	import os
	os.remove (DEST)

	return;

def CHECK_1 ():
	ADDRESS = "structs_1_1.JSON"

	try:
		DELETE_PATH (ADDRESS)
	except Exception as E:
		print (E)

	
	import cyte.structs.DB.access as access
	STRUCT_DB = access.DB (PATH (ADDRESS))
	
	import cyte.structs.scan.NAMES.has as STRUCT_HAS_NAME
	STRUCT = STRUCT_HAS_NAME.SEARCH (
		STRUCT_DB,
		NAME = "PROTEIN"
	)
	assert (len (STRUCT ["names"]) == 1)
	assert (STRUCT ["names"][0] == "protein")
		
	#
	#
	#
	
	import cyte.structs.sculpt.names as sculpt_NAMES
	sculpt_NAMES.START (
		STRUCT_DB,
		REGION = 1,
		NAMES = [ "protein", "proteina" ]
	)
	STRUCT = STRUCT_HAS_NAME.SEARCH (
		STRUCT_DB,
		NAME = "PROTEIN"
	)
	
	print (STRUCT)
	
	assert (len (STRUCT ["names"]) == 2)
	assert (STRUCT ["names"][0] == "protein")
	assert (STRUCT ["names"][1] == "proteina")
	
	#
	#
	#
	

	DELETE_PATH (ADDRESS)

	return;
	
CHECKS = {
	"CHECK 1": CHECK_1
}