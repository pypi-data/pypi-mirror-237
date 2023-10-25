


'''
import cyte.structs.DB.access as access
import cyte.structs.scan.NAMES.has as STRUCT_HAS_NAME
STRUCT = STRUCT_HAS_NAME.SEARCH (
	access.DB (),
	NAME = "PROTEIN"
)
'''

from tinydb import TinyDB, Query
import cyte.structs.DB.PATH as structs_DB_PATH

def SEARCH (
	structs_DB,
	NAME = "",
	
	RETURN_BOOL = False
):
	LIST = structs_DB.all ()
	
	NAME = NAME.lower ()
	
	for STRUCT in LIST:
		STRUCT_NAMES = STRUCT ["names"]
		
		for STRUCT_NAME in STRUCT_NAMES:
			if (NAME == STRUCT_NAME.lower ()):			
				Q = Query ()
				EL = structs_DB.get (Q.region == STRUCT ["region"])
				
				if (RETURN_BOOL == True):
					return True
				else:
					return EL
				
				
	if (RETURN_BOOL == True):
		return False
		
	raise Exception (f'name "{ NAME }" was not found.')
	