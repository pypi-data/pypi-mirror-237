



'''
	python3 STATUS.py "structs/scan/NAMES/has/STATUS_dynamic_1.py"
'''



def CHECK_1 ():
	import cyte.structs.DB.access as access
	import cyte.structs.scan.NAMES.has as STRUCT_HAS_NAME
	STRUCT = STRUCT_HAS_NAME.SEARCH (
		access.DB (),
		NAME = "PROTEIN"
	)
	
	print (STRUCT)

	import tinydb
	assert (type (STRUCT) == tinydb.table.Document)
	assert (STRUCT ["region"] == 1)
	
	
CHECKS = {
	"dynamic, has name": CHECK_1
}