

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
#	ATTACH { INNER } structURES
#
def ATTACH_INNER_structURES ():
	return



def FORMULATE (struct_DB):
	structs = structs_LIST.FIND (struct_DB)
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
			struct = structs [ SELECTOR ]
		
			if (len (struct ["PART OF"]) == 0):
				BRANCHES.append (struct)
				
				structs.remove (struct)	
				LAST_INDEX -= 1
				continue;				
			
			else:
				ATTACHED = ATTEMPT_TO_ATTACH.START (struct, BRANCHES)
				if (ATTACHED == True):
					structs.remove (struct)	
					LAST_INDEX -= 1
					continue;			
		
			SELECTOR += 1
	
	
		if (CYCLE == CYCLE_LIMIT):
			print ("CYCLE LIMIT REACHED", len (structs), "OF", structs_COUNT)
	
		CYCLE += 1

	SORT_TREES.START (BRANCHES)

	return BRANCHES