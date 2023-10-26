

'''
	python3 status.py "recipes/struct_2/_status/STATUS_recipe_1.py"
'''

import cyte.FOOD.USDA.examples as USDA_examples
import cyte.FOOD.USDA.struct_2 as USDA_struct_2

import cyte.supplements.NIH.examples as NIH_examples
import cyte.supplements.NIH.struct_2 as struct_2

import cyte.recipes.struct_2 as struct_2_recipes

def check_1 ():	
	walnuts_1882785 = USDA_struct_2.CALC (
		USDA_examples.RETRIEVE ("BRANDED/walnuts_1882785.json")
	)	
	calcium_261967 = struct_2.CALC (
		NIH_examples.RETRIEVE ("TABLETS/CALCIUM_261967.JSON")
	)
	
	struct_2_recipes.calc ({
		"products": [
			walnuts_1882785,
			calcium_261967
		]
	})

	return;
	
	
	
CHECKS = {
	"recipe 1": check_1
}