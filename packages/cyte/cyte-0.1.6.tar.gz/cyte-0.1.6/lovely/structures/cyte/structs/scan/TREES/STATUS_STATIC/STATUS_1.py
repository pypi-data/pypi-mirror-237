

'''
	python3 STATUS.py "structs/scan/TREES/STATUS_STATIC/STATUS_1.py"
'''

import cyte.structs.DB.access as access
import cyte.structs.scan.TREES as TREES

import json

def PATH ():
	import pathlib
	from os.path import dirname, join, normpath
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	return normpath (join (THIS_FOLDER, "structs.json"))

def CHECK_1 ():
	struct_DB = access.DB ()

	#struct_DB = access.DB (PATH (), sort_keys = True)
	struct_TREES = TREES.FORMULATE (struct_DB)
	print ("TREES", json.dumps (struct_TREES, indent = 4))

	#struct = FIND_struct (name = "CARBOHYDRATES")

	def PRINT_TREE (structs, INDENT = 0):
		for struct in structs:
		
			print (" " * INDENT, struct ["names"])
			
			if ("includes" in struct):
				PRINT_TREE (
					struct ["includes"], 
					INDENT = (INDENT + 4)
				)

	PRINT_TREE (struct_TREES)

	return;
	
	
	
CHECKS = {
	"CHECK 1": CHECK_1
}