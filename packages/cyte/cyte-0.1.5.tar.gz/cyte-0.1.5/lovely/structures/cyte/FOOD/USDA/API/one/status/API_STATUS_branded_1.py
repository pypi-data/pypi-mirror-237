

'''
python3 status_api.py "FOOD/USDA/API/one/status/API_STATUS_branded_1.py"
'''

from BOTANY.IMPORT import IMPORT

import json

import cyte.FOOD.USDA.API.one as USDA_FOOD_API

def CHECK_BRANDED_1 ():
	KEYS = IMPORT ("/ONLINE_KEYS/USDA/__init__.py").KEYS ()
	FOOD = USDA_FOOD_API.FIND (
		2642759,
		API_KEY = KEYS ["API"]
	)

	
CHECKS = {
	"CHECK BRANDED 1": CHECK_BRANDED_1
}