



'''
	python3 status.py "supplements/NIH/struct_2/_status_tablets/STATUS_PlantFusion_Calcium_261967.py"
'''

'''
	https://www.amazon.com/PlantFusion-Supports-Mineralized-Supplement-90/dp/B07VP749CF
'''

import json

import cyte.supplements.NIH.EXAMPLES as NIH_EXAMPLES
import cyte.supplements.NIH.struct_2 as struct_2

import cyte._ensure.eq as equality

def CHECK_1 ():
	supplement_struct_2 = struct_2.CALC (NIH_EXAMPLES.RETRIEVE ("TABLETS/CALCIUM_261967.JSON"))
	
	print ("supplement_struct_2:", json.dumps (supplement_struct_2, indent = 4))
	
	assert (supplement_struct_2 ["product"]["name"] == "Vegan Plant-Based Calcium 1,000 mg")
	assert (supplement_struct_2 ["product"]["DSLD"] == "261967")

	
	assert ("brand" in supplement_struct_2)
	assert ("name" in supplement_struct_2 ["brand"])
	assert (type (supplement_struct_2 ["brand"]["name"]) == str)
	
	assert (
		supplement_struct_2 ["defined"] ==
		{
			"serving size": {
				"quantity": 3
			}
		}
	)
	assert (
		supplement_struct_2 ["form"] ==
		{
			"unit": "Tablet",
			"quantity": 90
		}
	)
	

	
	equality.check (len (supplement_struct_2 ["ingredients"]["quantified grove"]), 9)

	equality.check (
		supplement_struct_2 ["ingredients"]["quantified grove"][7]["name"],
		"Vitamin D3"
	)
	equality.check (
		supplement_struct_2 ["ingredients"]["quantified grove"][7]["quantity per form"],
		{
			"form": "Tablet",
			"amount": "20/3",
			"unit": "mcg"
		}
	)
	equality.check (
		supplement_struct_2 ["ingredients"]["quantified grove"][7]["quantity per form, in grams"],
		{
			"form": "Tablet",
			"amount": "1/150000",
			"unit": "g"
		}
	)
	equality.check (
		supplement_struct_2 ["ingredients"]["quantified grove"][7]["quantity per package, in grams"],
		{
			"amount": "3/5000",
				"unit": "g"
		}
	)

	
	assert (len (supplement_struct_2 ["ingredients"]["unquantified"]) == 4)

	equality.check (
		supplement_struct_2 ["mass"] ["sum of quantified ingredients per package, exluding effectual"] ["grams"],
		"580153/375000"
	)
	equality.check (
		supplement_struct_2 ["mass"] ["sum of quantified ingredients per form, exluding effectual"] ["grams"],
		"580153/33750000"
	)
	
	#import pyjsonviewer
	#pyjsonviewer.view_data (json_data = supplement_struct_2)

	
	
CHECKS = {
	"CALCIUM 261967": CHECK_1
}