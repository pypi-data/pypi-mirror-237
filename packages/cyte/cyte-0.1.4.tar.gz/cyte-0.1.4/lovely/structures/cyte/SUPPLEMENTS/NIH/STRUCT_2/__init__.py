


'''
import cyte.FOOD.NIH.STRUCT_2 as STRUCT_2
RETURN = STRUCT_2.CALC ()
'''

import cyte.SUPPLEMENTS.NIH.STRUCT_2.FORM as FORM 
import cyte.SUPPLEMENTS.NIH.STRUCT_2.defined.serving_size_quantity as defined_serving_size_quantity 
import cyte.SUPPLEMENTS.NIH.STRUCT_2.ingredients.quantified as INGREDIENTS_QUANTIFIED 
import cyte.SUPPLEMENTS.NIH.STRUCT_2.mass.algorithm_1 as MASS_ALGORITHM_1

import json

def CALC (NIH_SUPPLEMENT_DATA):
	assert ("fullName" in NIH_SUPPLEMENT_DATA)
	assert ("brandName" in NIH_SUPPLEMENT_DATA)
	assert ("id" in NIH_SUPPLEMENT_DATA)

	RETURN = {
		"product": {
			"name":	NIH_SUPPLEMENT_DATA ["fullName"],
			"DSLD": str (NIH_SUPPLEMENT_DATA ["id"]),
			"UPC": NIH_SUPPLEMENT_DATA ["upcSku"]			
		},
		
		"brand": {
			"name":	NIH_SUPPLEMENT_DATA ["brandName"]
		},
		
		"form": {},
		
		"defined": {
			"serving size": {}
		},
		
		"ingredients": {
			"quantified list": [],
			"quantified grove": [],			
			"unquantified": []
		},
		
		"mass of quantified ingredients": {}
	}
	
	RETURN ["form"]["unit"] = FORM.CALC_UNIT (NIH_SUPPLEMENT_DATA)
	RETURN ["form"]["quantity"] = FORM.CALC_QUANTITY (NIH_SUPPLEMENT_DATA)

	RETURN ["defined"]["serving size"]["quantity"] = defined_serving_size_quantity.CALC (
		NIH_SUPPLEMENT_DATA
	)
	
	print ("RETURN:", json.dumps (RETURN, indent = 4))
	
	RETURN ["ingredients"]["quantified list"] = INGREDIENTS_QUANTIFIED.CALC (
		NIH_SUPPLEMENT_DATA,
		RETURN
	)
	
	RETURN ["ingredients"]["unquantified"] = NIH_SUPPLEMENT_DATA [
		"otheringredients"
	] [ "ingredients" ]
	
	
	RETURN [
		"mass of quantified ingredients"
	] = MASS_ALGORITHM_1.CALC (NIH_SUPPLEMENT_DATA, RETURN)

	return RETURN