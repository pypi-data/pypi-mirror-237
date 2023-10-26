
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