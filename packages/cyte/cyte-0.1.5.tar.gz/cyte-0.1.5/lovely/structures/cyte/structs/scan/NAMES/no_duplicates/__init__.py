
'''
raises an exception is a duplicate is found.
'''

'''
import cyte.structs.DB.access as access
from cyte.structs.scan.NAMES.no_duplicates import structs_NAMES_NO_DUPLICATES
structs_NAMES_NO_DUPLICATES (
	access.DB ()
)
'''

import cyte.structs.scan as STRUCT_scan

def structs_NAMES_NO_DUPLICATES (
	structs_DB
):
	NAMES = []

	def FOR_EACH (STRUCT):
		STRUCT_NAMES = STRUCT ["names"]
			
		for STRUCT_NAME in STRUCT_NAMES:
			STRUCT_NAME = STRUCT_NAME.lower ()
		
			if (STRUCT_NAME in NAMES):
				raise Exception (f"duplicate found: { STRUCT_NAME }")
		

	structs = STRUCT_scan.START (
		FOR_EACH = FOR_EACH
	)

