

'''
import cyte.structs.DB.access as access
import cyte.structs.scan.TREES as TREES
TREES = TREES.FORMULATE (access.DB ())
'''

'''
{
	"region": 3,

	"names": [
		"LIPIDS",
		"TOTAL LIPID (FAT)"
	],
	
	"PART OF": [],
	"includes": [
		{
			"PART OF": 3,
			"names": [
				"FATTY ACIDS, TOTAL SATURATED"
			],
			"region": 4
		}	
	]
},
'''


import cyte.structs.DB.access as access
import cyte.structs.scan.struct.list as structs_LIST
import cyte.structs.scan.TREES.FN.ATTEMPT_TO_ATTACH as ATTEMPT_TO_ATTACH
import cyte.structs.scan.TREES.SORT as SORT_TREES


import json


#
#	ATTACH { INNER } STRUCTURES
#
def ATTACH_INNER_STRUCTURES ():
	return



def FORMULATE (STRUCT_DB):
	structs = structs_LIST.FIND (STRUCT_DB)
	structs_COUNT = len (structs)
	
	print (json.dumps (structs, indent = 4))

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
		
			if (len (STRUCT ["PART OF"]) == 0):
				BRANCHES.append (STRUCT)
				
				structs.remove (STRUCT)	
				LAST_INDEX -= 1
				continue;				
			
			else:
				ATTACHED = ATTEMPT_TO_ATTACH.START (STRUCT, BRANCHES)
				if (ATTACHED == True):
					structs.remove (STRUCT)	
					LAST_INDEX -= 1
					continue;			
		
			SELECTOR += 1
	
	
		if (CYCLE == CYCLE_LIMIT):
			print ("CYCLE LIMIT REACHED", len (structs), "OF", structs_COUNT)
	
		CYCLE += 1

	SORT_TREES.START (BRANCHES)

	return BRANCHES