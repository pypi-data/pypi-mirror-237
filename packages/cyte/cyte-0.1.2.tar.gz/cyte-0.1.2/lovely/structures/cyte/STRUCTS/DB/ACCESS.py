

'''
Accessing the core DB:

	import cyte.STRUCTS.DB.ACCESS as ACCESS
	STRUCTS_DB = ACCESS.DB ()
'''

'''
Accessing another DB (replica, etc.):

	import cyte.STRUCTS.DB.ACCESS as ACCESS
	import cyte.STRUCTS.DB.PATH as STRUCTS_DB_PATH
	STRUCTS_DB = ACCESS.DB (
		PATH = STRUCTS_DB_PATH.FIND ()
	)
'''

from tinydb import TinyDB, Query
import cyte.STRUCTS.DB.PATH as STRUCTS_DB_PATH

def DB (
	PATH = STRUCTS_DB_PATH.FIND (),
	sort_keys = True
):
	DB = TinyDB (
		PATH, 
		sort_keys = sort_keys
	)
	
	return DB;