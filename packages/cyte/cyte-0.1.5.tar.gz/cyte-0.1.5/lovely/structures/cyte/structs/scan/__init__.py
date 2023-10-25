


'''

INCLUDES = "VITAMIN B"

def FOR_EACH (STRUCT):
	STRUCT_NAMES = STRUCT ["names"]
		
	for STRUCT_NAME in STRUCT_NAMES:
		STRUCT_NAME = STRUCT_NAME.upper ()
	
		if (STRUCT_NAME.__contains__ (INCLUDES)):
			#Q = Query ()
			#EL = db.get (Q.REGION == STRUCT ["region"])
			
			return True

	return True

import cyte.structs.DB.access as access
import cyte.structs.scan as STRUCT_scan
structs = STRUCT_scan.START (
	structs_DB = access.DB (),
	FOR_EACH = FOR_EACH
)
'''

from tinydb import TinyDB, Query
import cyte.structs.DB.PATH as structs_DB_PATH

def START (
	structs_DB = None,
	FOR_EACH = lambda : ()
):
	PATH = structs_DB_PATH.FIND ()

	db = TinyDB (PATH)
	LIST = db.all ()
	
	RETURNS = []
	
	for STRUCT in LIST:		
		if (FOR_EACH (STRUCT) == True):
			RETURNS.append (STRUCT)
				
	return RETURNS
	