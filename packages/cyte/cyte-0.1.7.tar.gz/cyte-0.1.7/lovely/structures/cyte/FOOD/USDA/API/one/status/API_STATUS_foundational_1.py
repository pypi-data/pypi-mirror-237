

'''
python3 status_api.py "FOOD/USDA/API/one/status/API_STATUS_foundational_1.py"
'''

from BOTANY.IMPORT import IMPORT

import json

import cyte.FOOD.USDA.API.one as USDA_FOOD_API


def CHECK_FOUNDATIONAL_1 ():
	KEYS = IMPORT ("/ONLINE_KEYS/USDA/__init__.py").KEYS ()
	
	# 2346404
	FOOD = USDA_FOOD_API.FIND (
		2515381,
		API_KEY = KEYS ["API"],
		KIND = "FOUNDATIONAL"
	)
	
	#print (json.dumps (FOOD ['DATA'], indent = 4))
	



	
CHECKS = {
	"CHECK FOUNDATIONAL 1": CHECK_FOUNDATIONAL_1
}