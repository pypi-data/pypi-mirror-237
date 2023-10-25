

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
	STRUCT_DB = access.DB ()

	#STRUCT_DB = access.DB (PATH (), sort_keys = True)
	STRUCT_TREES = TREES.FORMULATE (STRUCT_DB)
	print ("TREES", json.dumps (STRUCT_TREES, indent = 4))

	#STRUCT = FIND_STRUCT (NAME = "CARBOHYDRATES")

	def PRINT_TREE (structs, INDENT = 0):
		for STRUCT in structs:
		
			print (" " * INDENT, STRUCT ["names"])
			
			if ("includes" in STRUCT):
				PRINT_TREE (
					STRUCT ["includes"], 
					INDENT = (INDENT + 4)
				)

	PRINT_TREE (STRUCT_TREES)

	return;
	
	
	
CHECKS = {
	"CHECK 1": CHECK_1
}