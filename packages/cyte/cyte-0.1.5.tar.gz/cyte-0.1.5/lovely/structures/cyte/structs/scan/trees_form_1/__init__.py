

'''
	import cyte.structs.scan.trees_form_1 as trees_form_1
	trees = trees_form_1.start (STRUCT_DB)
'''

import cyte.structs.DB.access as access
import cyte.structs.scan.struct.list as structs_LIST

import json

'''
class grow:
	def __init__ (this):
		return;

	def find_region (region):
		return;
		
	def build_tree (region):
		return;
	
	pass;
	
tree = grow ()
'''
	
import copy

def start (
	STRUCT_DB
):
	if (type (STRUCT_DB) == list):
		structs = STRUCT_DB
	else:
		structs = structs_LIST.FIND (STRUCT_DB)
	
	
	
	# structs_to_add = copy.deepcopy (structs)
	
	structs_tally = len (structs)

	#
	#	this is a list of all the struct regions that have 
	#
	#	{
	#		1: 2	
	#	}
	#
	#	
	struct_region_tallies = {}


	def find_region (region):
		for struct in structs:
			if (struct ['region'] == region):
				return struct;
				
		raise Exception (f"'region' '{ region }' was not found in structs.")


	def build_tree (region):
		struct = find_region (region)	
		
		if (struct ["region"] in struct_region_tallies):
			print ('skipping', struct ['names'])
		
			return;
		else:
			struct_region_tallies [ struct ["region"] ] = 1
			print (struct_region_tallies)
		
		struct ["includes structs"] = []
		includes = struct ["includes"]		
		for include in includes:
			struct ["includes structs"].append (build_tree (include))
		
		return struct;

	print ("structs tally:", structs_tally)

	

	trees = []


	selector = 0
	last_index = len (structs) - 1
	while (selector <= last_index):		
		struct = structs [ selector ]
		
		if (struct ["region"] in struct_region_tallies):
			print ('skipping', struct ['names'])
			selector += 1
			continue;
		else:
			struct_region_tallies [ struct ["region"] ] = 1
		
		struct ["includes structs"] = []
		includes = struct ["includes"]		
		for include in includes:
			struct ["includes structs"].append (build_tree (include))

		trees.append (struct)
		
		selector += 1
		
		
	return trees;
	
