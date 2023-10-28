

'''
import cyte.recipes.struct_2 as struct_2_recipes
import cyte.structs.DB.access as access
import cyte.structs.scan.trees_form_1 as trees_form_1

struct_2_recipes.calc ({
	"products": [
		{
			"product": { "FDC ID": "" }
		},
		{
			"product": { "DSLD": "" }
		}
	],
	"structs grove": trees_form_1.start (access.DB ())
})
'''


import cyte.recipes.struct_2.ingredients.quantified_grove.aggregator as quantified_grove_aggregator

def calc (delivery):
	products = delivery ["products"]
	#structs_grove = delivery ["structs grove"]
	
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
	
		quantified_grove_aggregator.calc (
			recipe_quantified_grove,
			product ["ingredients"]["quantified grove"],
		)

	return;