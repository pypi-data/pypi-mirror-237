
'''
	python3 STATUS.py "structs/scan/NAMES/no_duplicates/STATUS_DYNAMIC_1.py"
'''

def CHECK_1 ():
	import cyte.structs.DB.access as access
	from cyte.structs.scan.NAMES.no_duplicates import structs_NAMES_NO_DUPLICATES
	structs_NAMES_NO_DUPLICATES (
		access.DB ()
	)
	
CHECKS = {
	"dynamic, no duplicates found": CHECK_1
}