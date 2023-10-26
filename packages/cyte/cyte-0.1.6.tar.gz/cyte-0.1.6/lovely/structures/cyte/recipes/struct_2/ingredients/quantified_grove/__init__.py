
'''
import cyte.recipes.struct_2.ingredients.quantified_grove as quantified_grove_aggregator
quantified_grove_aggregator.calc ()
'''

import cyte.structs.scan.names.has as struct_has_name

import json

def attach_struct (
	product_structs = [], 
	structs_db = None,
	level = 0
):
	indent = " " * (level * 4)
	product_structs.sort (key = lambda product_struct : product_struct ["name"][0])

	for product_struct in product_structs:	
		struct = struct_has_name.search (
			structs_db,
			name = nih_struct ['name']
		)

		print (f"{ indent }{ product_struct ['name'] } : r{ struct ['region'] }")

		if ("nestedRows" in product_struct):
			print_grove (
				product_struct ["nestedRows"], 
				level = (level + 1),
				
				structs_db = structs_db
			)
			

def add (
	recipe_quantified_grove,
	ingredient_quantified_grove
):
	print ("ingredient_quantified_grove:", json.dumps (ingredient_quantified_grove, indent = 4))
	print ()

	return;

	attach_struct (
		product_structs = ingredient_quantified_grove
	)

	return;