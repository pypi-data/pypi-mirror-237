
'''
	import cyte.FOOD.USDA.examples as USDA_examples
	import cyte.FOOD.USDA.struct_2 as USDA_struct_2
	walnuts_1882785 = USDA_struct_2.CALC (
		USDA_examples.RETRIEVE ("BRANDED/walnuts_1882785.json")
	)
'''

'''
	import cyte.FOOD.USDA.examples as USDA_examples
	EXAMPLE = USDA_examples.RETRIEVE ("BRANDED/BEET_JUICE_2642759.JSON")
'''


def RETRIEVE (PATH):
	import pathlib
	from os.path import dirname, join, normpath

	THIS_FOLDER = pathlib.Path (__file__).parent.resolve ()
	EXAMPLE = normpath (join (THIS_FOLDER, PATH))

	import json
	with open (EXAMPLE) as FP:
		DATA = json.load (FP)
	

	return DATA