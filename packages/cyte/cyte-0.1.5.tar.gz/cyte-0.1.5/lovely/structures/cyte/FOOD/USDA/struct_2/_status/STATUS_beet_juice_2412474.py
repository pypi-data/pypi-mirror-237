



'''
	python3 status.py "FOOD/USDA/struct_2/_status/STATUS_beet_juice_2412474.py"
'''

import json

import cyte.FOOD.USDA.EXAMPLES as USDA_EXAMPLES
import cyte.FOOD.USDA.struct_2 as USDA_struct_2

import cyte._ensure.eq as equality

def CHECK_1 ():
	food_struct_2 = USDA_struct_2.CALC (
		USDA_EXAMPLES.RETRIEVE ("BRANDED/BEET_JUICE_2412474.JSON")
	)
	
	#import pyjsonviewer
	#pyjsonviewer.view_data (json_data = food_struct_2)

	assert (food_struct_2 ["volume"]["per package, in liters"] == "0.473176")
	assert (
		food_struct_2 ["ingredients"]["unquantified string"] == 
		"BEET, CITRIC ACID"
	)
	
	
	equality.check (1, 1)
	
CHECKS = {
	"BEET JUICE 2642759": CHECK_1
}


