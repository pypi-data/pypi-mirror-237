


'''
https://fdc.nal.usda.gov/fdc-app.html#/food-details/1882785/nutrients
'''



'''
	python3 status.py "FOOD/USDA/struct_2/_status/STATUS_walnuts_1882785.py"
'''

import json

import cyte.FOOD.USDA.EXAMPLES as USDA_EXAMPLES

import cyte.FOOD.USDA.struct_2 as USDA_struct_2
import cyte.FOOD.USDA.struct_2.ingredients.quantified_grove.printer as quantified_grove_printer


def CHECK_1 ():
	EXAMPLE = USDA_EXAMPLES.RETRIEVE ("BRANDED/walnuts_1882785.json")
	returns = USDA_struct_2.CALC (EXAMPLE)
	
	print (json.dumps (returns, indent = 4))

	import pyjsonviewer
	pyjsonviewer.view_data (json_data = returns)
	
	ingredients_quantified_grove = returns ["ingredients"]["quantified grove"]
	
	quantified_grove_printer.start (ingredients_quantified_grove)
	
	
	
CHECKS = {
	"walnuts 1882785": CHECK_1
}


