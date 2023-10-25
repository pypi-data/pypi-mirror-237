


'''
import cyte.structs.scan.net as net_build
struct_net = net_build.start ()
'''

'''
{
	"names": [
		"carbohydrates",
		"carbohydrate, by difference"
	],
	"region": 2,
	"includes": [ 7 ]
}
'''

import cyte.structs.DB.access as access
import cyte.structs.scan.struct.list as structs_LIST

import json

def find_included (struct_to_find, structs):
	#for struct in structs:
	#	if 

	return

def start (STRUCT_DB):
	structs = structs_LIST.FIND (STRUCT_DB)
	structs_COUNT = len (structs)

	print ("structs count:", structs_COUNT)

	BRANCHES = []

	CYCLE_LIMIT = 20
	CYCLE = 1
	while (
		len (structs) >= 1 and
		CYCLE <= CYCLE_LIMIT
	):
		SELECTOR = 0
		LAST_INDEX = len (structs) - 1
		while (SELECTOR <= LAST_INDEX):
			STRUCT = structs [ SELECTOR ]
		
			includes = STRUCT ["includes"]
			
			if (len (includes) >= 1):
				print ('includes:', includes)
				
				included = find_included (STRUCT, structs)
			
			
			
			SELECTOR += 1
		
		
		if (CYCLE == CYCLE_LIMIT):
			print ("cycle limit reached", len (structs), "of", structs_COUNT)
	
		CYCLE += 1











