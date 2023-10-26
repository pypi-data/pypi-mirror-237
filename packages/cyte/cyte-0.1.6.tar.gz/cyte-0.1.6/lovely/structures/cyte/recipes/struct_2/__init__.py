

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
	
	
	'''
		attach [nih,usda] ingredient groves to struct trees_form_1
		
			example:
				data:
					walnuts, 20g
						dietary fiber, 7g
					
					lentils, 28g
						carbs 12g
							dietary fiber, 6g
							
				trees_form_1
					carbohydrates [not found]
						dietary fiber, 7g
						
					carbohydrates 12g
						dietary fiber, 6g
						
				add summation of descend struct masses to ascendent structs if not found.
					carbohydrates 7g
						dietary fiber, 7g
						
					carbohydrates 12g
						dietary fiber, 6g
	'''
	'''
		[{
			
			
		}]
	'''
	recipe_quantified_grove = []	
	for product in products:
		print (product ["product"]["name"])
	
		quantified_grove_aggregator.add (
			recipe_quantified_grove,
			product ["ingredients"]["quantified grove"]
		)

	return;