



'''
	python3 STATUS.py "structs/scan/trees_form_1/status/STATUS_1.py"
'''

import cyte.structs.DB.access as access

import json

def PATH ():
	import pathlib
	from os.path import dirname, join, normpath
	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	return normpath (join (THIS_FOLDER, "structs.json"))

def CHECK_1 ():
	STRUCT_DB = access.DB (PATH (), sort_keys = True)

	import cyte.structs.scan.trees_form_1 as trees_form_1
	trees = trees_form_1.start (STRUCT_DB)
	
	import json
	print (json.dumps (trees, indent = 4))
	
	
	the_grove = ""
	def print_trees (trees, level):
		nonlocal the_grove;
	
		for tree in trees:
			names = tree ['names']
			indent = "  " * level
		
			print (f'{ indent }{ names }')
			the_grove += f'{ indent }{ str (names) }\n'
			
			if ("includes structs" in tree):
				print_trees (tree ["includes structs"], level = level + 1)
	
	print_trees (trees, level = 0)
	
	
	import json

	import pathlib
	from os.path import dirname, join, normpath
	THIS_FOLDER = str (pathlib.Path (__file__).parent.resolve ())
	with open (THIS_FOLDER + '/the_grove.json') as f:	
	
		grove = json.load (f)["grove"]
	
		assert (grove == trees)
	
	#print (the_grove)

	
CHECKS = {
	"CHECK 1": CHECK_1
}