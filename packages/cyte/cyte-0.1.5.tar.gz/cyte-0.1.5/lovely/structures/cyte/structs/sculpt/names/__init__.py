


'''
import cyte.structs.DB.access as access
import cyte.structs.sculpt.names as sculpt_NAMES

STRUCT_DB = access.DB ()
sculpt_NAMES.START (
	STRUCT_DB,
	REGION = 10000,
	NAMES = []
)
'''


from tinydb import TinyDB, Query

def START (
	sculpt_DB,
	REGION,
	NAMES
):
	Q = Query ()
	sculpt_DB.update (
		{ 
			'names': NAMES
		}, 
		Q.region == REGION
	)

	return;