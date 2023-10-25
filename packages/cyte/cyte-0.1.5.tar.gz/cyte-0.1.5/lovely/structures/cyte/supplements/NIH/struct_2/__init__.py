


'''
import cyte.FOOD.NIH.struct_2 as struct_2
RETURN = struct_2.CALC ()
'''

import cyte.supplements.NIH.struct_2.form as form 
import cyte.supplements.NIH.struct_2.form.unit as form_unit
import cyte.supplements.NIH.struct_2.defined.serving_size_quantity as defined_serving_size_quantity 
import cyte.supplements.NIH.struct_2.ingredients.quantified as INGREDIENTS_QUANTIFIED 
import cyte.supplements.NIH.struct_2.mass.algorithm_1 as mass_algorithm_1

import json

def CALC (nih_supplement_data):
	assert ("fullName" in nih_supplement_data)
	assert ("brandName" in nih_supplement_data)
	assert ("id" in nih_supplement_data)

	RETURN = {
		"product": {
			"name":	nih_supplement_data ["fullName"],
			"DSLD": str (nih_supplement_data ["id"]),
			"UPC": nih_supplement_data ["upcSku"]			
		},
		
		"brand": {
			"name":	nih_supplement_data ["brandName"]
		},
		
		"form": {},
		
		"defined": {
			"serving size": {}
		},
		
		"ingredients": {
			"quantified grove": [],			
			"unquantified": []
		},
		
		"mass": {
			"of quantified ingredients, including effectual": {},
			"of quantified ingredients, excluding effectual": {},
		}
	}
	
	RETURN ["form"]["unit"] = form_unit.calc (nih_supplement_data)
	RETURN ["form"]["quantity"] = form.CALC_QUANTITY (nih_supplement_data)

	RETURN ["defined"]["serving size"]["quantity"] = defined_serving_size_quantity.CALC (
		nih_supplement_data
	)
	
	print ("RETURN:", json.dumps (RETURN, indent = 4))
	
	RETURN ["ingredients"]["quantified grove"] = INGREDIENTS_QUANTIFIED.CALC (
		nih_supplement_data,
		RETURN
	)
	
	RETURN ["ingredients"]["unquantified"] = nih_supplement_data [
		"otheringredients"
	] [ "ingredients" ]
	

	
	calculated_masses = mass_algorithm_1.CALC (nih_supplement_data, RETURN)
	print ("calculated_masses masses", calculated_masses)
	
	for calculated in calculated_masses:
		RETURN ["mass"][ calculated ] = calculated_masses [ calculated ]

	return RETURN