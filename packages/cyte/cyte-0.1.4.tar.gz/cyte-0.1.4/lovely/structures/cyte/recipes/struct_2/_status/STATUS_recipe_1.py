

'''
	python3 status.py "recipes/struct_2/_status/STATUS_recipe_1.py"
'''

import cyte.FOOD.USDA.EXAMPLES as USDA_EXAMPLES
import cyte.FOOD.USDA.STRUCT_2 as USDA_STRUCT_2

import cyte.SUPPLEMENTS.NIH.EXAMPLES as NIH_EXAMPLES
import cyte.SUPPLEMENTS.NIH.STRUCT_2 as STRUCT_2

import cyte.recipes.struct_2 as struct_2_recipes

def check_1 ():	
	BEET_JUICE_2412474 = USDA_STRUCT_2.CALC (
		USDA_EXAMPLES.RETRIEVE ("BRANDED/BEET_JUICE_2412474.JSON")
	)	
	MULTIVITAMIN_276336 = STRUCT_2.CALC (
		NIH_EXAMPLES.RETRIEVE ("COATED TABLETS/MULTIVITAMIN_276336.JSON")
	)
	
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

	return;
	
	
	
CHECKS = {
	"recipe 1": check_1
}