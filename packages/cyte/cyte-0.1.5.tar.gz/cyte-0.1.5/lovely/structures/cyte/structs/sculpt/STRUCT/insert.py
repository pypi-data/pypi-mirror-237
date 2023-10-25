


'''
import cyte.structs.DB.access as access
import cyte.structs.sculpt.STRUCT.insert as STRUCT_INSERT
structs = STRUCT_INSERT.START (
	access.DB (),
	{
		'PART OF': [], 
		"names": [ '' ]
	}
)
'''

import cyte.structs.DB.access as access
import cyte.structs.scan.regions.find_next as FIND_NEXT_REGION


def START (STRUCT_DB, STRUCT):
	NEXT_REGION = FIND_NEXT_REGION.START (
		STRUCT_DB
	)
	
	STRUCT ["region"] = NEXT_REGION
	ID = STRUCT_DB.insert (STRUCT)
	assert (type (ID) == int)
