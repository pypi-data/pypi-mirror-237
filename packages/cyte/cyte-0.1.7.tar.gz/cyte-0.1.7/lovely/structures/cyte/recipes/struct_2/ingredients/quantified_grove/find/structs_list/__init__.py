


'''
import cyte.recipes.struct_2.ingredients.quantified_grove.find.structs_list as structs_list
structs_list.start ()
'''

import cyte.structs.scan.names.has as struct_has_name
import json

def start (
	structs_db = None,
	product_structs = [], 
	level = 0,
	skipped = [],
	structs_list = []
):
	indent = " " * (level * 4)
	product_structs.sort (
		key = lambda product_struct : product_struct ["name"][0]
	)

	for product_struct in product_structs:	
		try:
			struct = struct_has_name.search (
				structs_db,
				name = product_struct ['name']
			)
		except Exception as E:
			skipped.append (product_struct ['name'])
			return;
			
		structs_list.append (struct)

		#print (f"{ indent }{ product_struct ['name'] } : r{ struct ['region'] }")

		print (product_struct ['name'], len (product_struct ["quantified grove"]))

		if ("quantified grove" in product_struct):
			start (
				structs_db = structs_db,
				product_structs = product_struct ["quantified grove"], 
				level = (level + 1),
				skipped = skipped,
				structs_list = structs_list
			)