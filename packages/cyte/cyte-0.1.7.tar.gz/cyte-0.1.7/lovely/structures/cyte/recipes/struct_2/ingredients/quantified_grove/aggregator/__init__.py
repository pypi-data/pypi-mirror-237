
'''
This adds products to the recipe.
'''

'''
import cyte.recipes.struct_2.ingredients.quantified_grove.aggregator as quantified_grove_aggregator
quantified_grove_aggregator.calc (
	recipe_quantified_grove = [],
	product_quantified_grove = []
)
'''


import json
	
import cyte.recipes.struct_2.ingredients.quantified_grove.find.structs_list as find_structs_list

import cyte.structs.DB.access as access
import cyte.structs.scan.names.has as struct_has_name
import cyte.structs.scan.trees_form_1 as trees_form_1
	
	
def calc (
	recipe_quantified_grove,
	product_quantified_grove
):
	skipped = []
	product_structs_list = []
	structs_db_1 = access.DB ()

	find_structs_list.start (
		structs_db = structs_db_1,
		product_structs = product_quantified_grove,
		structs_list = product_structs_list,
		skipped = skipped
	)

	print ("structs found:");
	for struct in product_structs_list:
		print (" ", struct ["names"])


	print ("skipped:", json.dumps (skipped, indent = 4))

	#
	#	structs_db_1 dict shouldn't be modified, but in case it is,
	#	utilize a difference one.
	#
	structs_db_2 = access.DB ()
	trees_form_1_grove = trees_form_1.start (structs_db_2)

	import cyte.structs.scan.trees_form_1.printer as trees_form_1_printer
	trees_form_1_printer.write (trees_form_1_grove)

	#
	#	attach the "product structs" to the "structs tree form 1"
	#
	for product_struct in product_structs_list:
		pass;

	return {
		"product structs list": product_structs_list
	}