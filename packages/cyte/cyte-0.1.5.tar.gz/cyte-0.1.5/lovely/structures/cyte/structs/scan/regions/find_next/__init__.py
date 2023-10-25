
'''
import cyte.structs.DB.access as access
import cyte.structs.scan.regions.find_next as FIND_NEXT_REGION
NEXT_REGION = FIND_NEXT_REGION.START (
	access.DB ()
)
'''

def START (STRUCT_DB):
	import cyte.structs.DB.access as access
	import cyte.structs.scan.struct.list as structs_LIST
	LIST = structs_LIST.FIND (STRUCT_DB)
	
	LIST.sort (key = lambda STRUCT : STRUCT ["region"])
	
	LAST_INDEX = len (LIST) - 1;
	
	return LIST [ LAST_INDEX ][ "region" ] + 1
	
	