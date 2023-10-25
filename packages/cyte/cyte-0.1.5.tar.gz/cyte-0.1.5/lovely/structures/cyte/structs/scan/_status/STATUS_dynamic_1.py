

'''
python3 STATUS.py "structs/scan/_STATUS/STATUS_dynamic_1.py"
'''


def CHECK_1 ():
	INCLUDES = "VITAMIN B1"

	def FOR_EACH (STRUCT):
		STRUCT_NAMES = STRUCT ["names"]
			
		for STRUCT_NAME in STRUCT_NAMES:
			STRUCT_NAME = STRUCT_NAME.upper ()
		
			if (STRUCT_NAME == INCLUDES.upper ()):
				return True

		return False

	import cyte.structs.DB.access as access
	import cyte.structs.scan as STRUCT_scan
	structs = STRUCT_scan.START (
		structs_DB = access.DB (),
		FOR_EACH = FOR_EACH
	)
	
	print ("structs:", structs)

	return;
	
	
CHECKS = {
	"check 1": CHECK_1
}