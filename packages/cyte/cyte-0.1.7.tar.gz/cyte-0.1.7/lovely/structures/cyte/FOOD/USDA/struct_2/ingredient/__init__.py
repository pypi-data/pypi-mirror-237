
'''
These are based on a portion of 100
	"defined": {
		"servings per package": "1.9715666666666667",
		"serving size": {
			"unit": "ml",
			"amount": "240"
		}
	}
	"mass": {
		"calculated": false
	},
	"volume": {
		"calculated": true,
		"per package, in liters": "0.473176"
	},
'''

'''
import cyte.FOOD.USDA.struct_2.ingredients.quantified_list.ingredient as quantified_ingredient
'''

'''
These are based on serving size:
	"labelNutrients": {
		"iron": {
			"value": 1.08
		}
	}
'''

'''

'''

import cyte.structs.DB.access as access
import cyte.structs.scan.names.has as struct_HAS_name
import cyte._interpret.unit_kind as UNIT_KIND
import cyte.mass.swap as mass_swap
	
	
from fractions import Fraction

#
#	??
#		either 100mL or 100g
#
PORTION = 100

def CALC (
	FOOD_NUTRIENT,
	usda_food_data_CALCULATED
):
	include_float = True;
	include_fraction_string = True
	include_fraction_string_grams = True
	include_float_grams = True

	name = FOOD_NUTRIENT ["nutrient"] ["name"]
	
	print ("food nutrient:", FOOD_NUTRIENT)
	
	assert ("amount" in FOOD_NUTRIENT), FOOD_NUTRIENT;
	assert ("unitName" in FOOD_NUTRIENT ["nutrient"]), FOOD_NUTRIENT;
	unit = FOOD_NUTRIENT ["nutrient"]["unitName"]
	
	nutrient_unit_kind = UNIT_KIND.CALC (unit)
	
	'''
		find the struct with that name,
		in the structs DB
	'''
	struct = struct_HAS_name.search (
		access.DB (),
		name = name
	)
	names = struct ["names"]
		
	servings_per_package = Fraction (usda_food_data_CALCULATED ["defined"][
		"servings per package, fraction string"
	])
	amount_in_serving = Fraction (usda_food_data_CALCULATED ["defined"]["serving size"]["amount"])
	amount_per_package = (
		Fraction (FOOD_NUTRIENT ["amount"]) /
		PORTION				
	) * servings_per_package * amount_in_serving
	
	amount_per_serving = (
		Fraction (FOOD_NUTRIENT ["amount"]) /
		PORTION				
	) * amount_in_serving

	'''
		"effectual mass per package": {}
	'''

	returns = {
		"name": name,
		"struct": struct,
	}
	
	
	if (nutrient_unit_kind == "energy"):
		return "energy"
	
	elif (nutrient_unit_kind == "mass"):	
		fraction_in_grams = mass_swap.START ([ amount_per_package, unit ], "grams");
	
		returns ["mass"] = {
			"per package": {
				** ({
					"float": {
						"amount": float (amount_per_package),
						"unit": unit
					}
				} if include_float else {}),
				** ({
					"fraction string": {
						"amount": str (amount_per_package),
						"unit": unit
					}
				} if include_fraction_string else {}),
				** ({
					"fraction string grams": str (fraction_in_grams)
				} if include_fraction_string_grams else {}),
				** ({
					"float grams": float (fraction_in_grams)
				} if include_float_grams else {}),
			},
			"per serving": {
				** ({
					"float": {
						"amount": float (amount_per_serving),
						"unit": unit
					}
				} if include_float else {}),
				** ({
					"fraction string": {
						"amount": str (amount_per_serving),
						"unit": unit
					}
				} if include_fraction_string else {})
			}
		}
		
	elif (nutrient_unit_kind == "effectual mass"):
		returns ["effectual mass"] = {
			"per package": {
				** ({
					"float": {
						"amount": float (amount_per_package),
						"unit": unit
					}
				} if include_float else {}),
				** ({
					"fraction string": {
						"amount": str (amount_per_package),
						"unit": unit
					}
				} if include_fraction_string else {}),
			},
			"per serving": {
				** ({
					"float": {
						"amount": float (amount_per_serving),
						"unit": unit
					}
				} if include_float else {}),
				** ({
					"fraction string": {
						"amount": str (amount_per_serving),
						"unit": unit
					}
				} if include_fraction_string else {})
			}
		}
		
	elif (nutrient_unit_kind == "volume"):	
		raise Exception (f"A nutrient was found that has volume units. { FOOD_NUTRIENT }")
		
	
	else:
		raise Exception (f"The nutrient unit kind '{ nutrient_unit_kind }' was not accounted for. { FOOD_NUTRIENT }")	
	
	
	
	return returns;