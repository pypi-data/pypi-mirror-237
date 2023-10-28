

'''
	python3 status.py "recipes/struct_2/ingredients/quantified_grove/aggregator/_status/STATUS_1.py"
'''



'''
	python3 status.py "recipes/struct_2/ingredients/quantified_grove/aggregator/_status/STATUS_1.py"
'''

import cyte.supplements.NIH.struct_2 as NIH_struct_2
import cyte.supplements.NIH.examples as NIH_examples

import cyte.recipes.struct_2.ingredients.quantified_grove.aggregator as quantified_grove_aggregator

def check_1 ():
	chia_seeds_214893 = NIH_struct_2.CALC (NIH_examples.RETRIEVE ("other/chia_seeds_214893.json"))

	recipe_quantified_grove = []
	returns = quantified_grove_aggregator.calc (
		recipe_quantified_grove = recipe_quantified_grove,
		product_quantified_grove = chia_seeds_214893 ["ingredients"] ["quantified grove"]
	)
	
	product_structs_list = returns ["product structs list"]
	assert (len (product_structs_list) == 21)


	return;
	
	
CHECKS = {
	"aggregator": check_1
}