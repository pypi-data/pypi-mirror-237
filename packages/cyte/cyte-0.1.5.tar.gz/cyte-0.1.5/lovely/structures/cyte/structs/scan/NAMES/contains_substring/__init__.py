
'''
	contains substring
'''

'''
import cyte.structs.DB.access as access
import cyte.structs.scan.NAMES.contains_substring as structs_WHERE_NAME_CONTAINS_SUBSTRING
structs = structs_WHERE_NAME_CONTAINS_SUBSTRING.FIND (
	access.DB (),
	"VITAMIN B"
)
'''

import cyte.structs.scan as STRUCT_scan

def FIND (
	structs_DB,
	CONTAINS
):
	CONTAINS = CONTAINS.upper ()

	def FOR_EACH (STRUCT):
		STRUCT_NAMES = STRUCT ["names"]
			
		for STRUCT_NAME in STRUCT_NAMES:
			STRUCT_NAME = STRUCT_NAME.upper ()
		
			if (STRUCT_NAME.__contains__ (CONTAINS)):
				#Q = Query ()
				#EL = db.get (Q.REGION == STRUCT ["region"])
				
				return True

		return False
	
	structs = STRUCT_scan.START (
		FOR_EACH = FOR_EACH
	)


	return structs