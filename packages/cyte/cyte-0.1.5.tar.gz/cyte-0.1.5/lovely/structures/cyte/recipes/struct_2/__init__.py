

'''
import cyte.recipes.struct_2 as struct_2_recipes
struct_2_recipes.calc ()
'''

'''
plan:
	struct_2_recipes.calc ({
		"products": [
			{
				"product": { "FDC ID": "" }
			},
			{
				"product": { "DSLD": "" }
			}
		]
	})
'''


import cyte.recipes.struct_2.ingredients.quantified_grove as quantified_grove_aggregator


def calc (delivery):
	products = delivery ["products"]
	
	recipe_quantified_grove = {}	
	for product in products:
		quantified_grove_aggregator.add (
			recipe_quantified_grove,
			product ["ingredients"]["quantified grove"]
		)

	return;