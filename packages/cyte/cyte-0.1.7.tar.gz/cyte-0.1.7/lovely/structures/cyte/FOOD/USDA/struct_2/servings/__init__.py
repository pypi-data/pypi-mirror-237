

'''
	"servingSize": 240,
	"servingSizeUnit": "ml",
'''

import json
from fractions import Fraction

import cyte.volume.swap as VOLUME_swap
import cyte.mass.swap as mass_swap	
	
def CALC (usda_food_data, usda_food_data_calculated):
	assert ("servingSize" in usda_food_data)
	assert ("servingSizeUnit" in usda_food_data)
	
	SERVING_SIZE_UNIT = usda_food_data ["servingSizeUnit"]
	SERVING_SIZE = usda_food_data ["servingSize"]
	
	import cyte._interpret.unit_kind as UNIT_KIND
	KIND = UNIT_KIND.CALC (SERVING_SIZE_UNIT)
	
	if (KIND == "volume"):
		if ("per package, in liters" in usda_food_data_calculated ["volume"]):
			LITERS_PER_SERVING = VOLUME_swap.START ([ SERVING_SIZE, SERVING_SIZE_UNIT ], "LITER")
			
			SERVINGS_PER_PACKAGE = str (
				Fraction (
					Fraction (usda_food_data_calculated ["volume"] ["per package, in liters"]),
					Fraction (LITERS_PER_SERVING)
				)
			)
		
		else:
			
		
			raise Exception ('serving size is in volume, but package volume is not known.')
		
		
	elif (KIND == "mass"):
		print (json.dumps (usda_food_data_calculated, indent = 4))
	
		mass = usda_food_data_calculated ["mass"];
	
		if ("per package, in grams" in mass):
			grams_per_serving = mass_swap.START ([ 
				SERVING_SIZE, 
				SERVING_SIZE_UNIT 
			], "GRAMS")
			
			SERVINGS_PER_PACKAGE = str (
				Fraction (
					Fraction (mass ["per package, in grams"]),
					Fraction (grams_per_serving)
				)
			)
		
		else:	
			raise Exception ('serving size is in "mass", but package "mass" is not known.')
	
		pass;
		
	else:
		raise Exception (f'Kind, received "{ KIND }", of serving size unit needs to be "volume" or "mass".')
	
	

	return SERVINGS_PER_PACKAGE