

'''
	python3 status.py "recipes/struct_2/_status/STATUS_recipe_1.py"
'''

'''
	零: 0
	一: 1
	二: 2
	三: 3
	四: 4
	五: 5
	六: 6
	七: 7
	八: 8
	九: 9
	十: 10
	
	朋友: friend
	梦: dreams
	梦想: dream
	钱: money
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
	chia_seeds_214893 = struct_2.CALC (NIH_examples.RETRIEVE ("other/chia_seeds_214893.json"))
	
	returns = struct_2_recipes.calc ({
		"products": [
			chia_seeds_214893
		]
	})
	
	#structs_list = returns ["structs list"]
	#assert (len (structs_list) == 21)

	return;
	
	
	
CHECKS = {
	"recipe 1": check_1
}