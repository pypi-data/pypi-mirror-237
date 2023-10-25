

import cyte._interpret.unit_kind as UNIT_KIND

import cyte.FOOD.USDA.struct_2.energy as ENERGY
import cyte.FOOD.USDA.struct_2.ingredients.quantified_list as quantified_list
import cyte.FOOD.USDA.struct_2.ingredients.quantified_grove as quantified_grove
import cyte.FOOD.USDA.struct_2.mass as MASS
import cyte.FOOD.USDA.struct_2.packageWeight as PACKAGE_WEIGHT
import cyte.FOOD.USDA.struct_2.servings as SERVINGS

def CALC (usda_food_data):
	returns = {
		"product": {
			"name":	usda_food_data ["description"],
			"FDC ID": str (usda_food_data ["fdcId"]),
			"UPC": usda_food_data ["gtinUpc"]			
		},
		
		"brand": {
			"name":	usda_food_data ["brandName"],
			"owner": usda_food_data ["brandOwner"]
		},
		
		"defined": {
			"servings per package": {},
			"serving size": {
				"unit": usda_food_data ["servingSizeUnit"],
				"amount": str (usda_food_data ["servingSize"]),
				"kind": UNIT_KIND.CALC (usda_food_data ["servingSizeUnit"])
			},
			"quantity": {
				"reported": usda_food_data ["packageWeight"],
				"notes": "This could be the 'mass' and or 'volume', etc."
			}			
		},
		
		"mass": {},
		"volume": {},
	
		"ingredients": {
			"quantified list": [],
			"quantified grove": [],
			
			"unquantified": [],
			"unquantified string": usda_food_data ["ingredients"]
		}
		
	}
	
	INTERPRETTED_PACKAGE_WEIGHT = PACKAGE_WEIGHT.INTERPRET (usda_food_data)
	if ("mass" in INTERPRETTED_PACKAGE_WEIGHT):
		returns ["mass"] = INTERPRETTED_PACKAGE_WEIGHT ["mass"]

	if ("volume" in INTERPRETTED_PACKAGE_WEIGHT):
		returns ["volume"] = INTERPRETTED_PACKAGE_WEIGHT ["volume"]

	returns ["defined"] ["servings per package"] = SERVINGS.CALC (usda_food_data, returns)

	returns ["ingredients"]["quantified list"] = quantified_list.calc (
		usda_food_data,
		returns
	)
	returns ["ingredients"]["quantified grove"] = quantified_grove.calc (
		usda_food_data,
		returns
	)

	return returns