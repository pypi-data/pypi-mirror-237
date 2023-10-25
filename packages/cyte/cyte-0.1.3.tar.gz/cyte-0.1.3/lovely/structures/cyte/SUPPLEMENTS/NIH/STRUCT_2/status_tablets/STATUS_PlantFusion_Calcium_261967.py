



'''
	python3 status.py "SUPPLEMENTS/NIH/STRUCT_2/status_tablets/STATUS_PlantFusion_Calcium_261967.py"
'''

'''
	https://www.amazon.com/PlantFusion-Supports-Mineralized-Supplement-90/dp/B07VP749CF
'''

import json

import cyte.SUPPLEMENTS.NIH.EXAMPLES as NIH_EXAMPLES
import cyte.SUPPLEMENTS.NIH.STRUCT_2 as STRUCT_2

import cyte._ensure.eq as EQ


def CHECK_1 ():
	EXAMPLE = NIH_EXAMPLES.RETRIEVE ("TABLETS/CALCIUM_261967.JSON")
	RETURN = STRUCT_2.CALC (EXAMPLE)
	
	print ("RETURN:", json.dumps (RETURN, indent = 4))
	
	assert (RETURN ["product"]["name"] == "Vegan Plant-Based Calcium 1,000 mg")
	assert (RETURN ["product"]["DSLD"] == "261967")

	
	assert ("brand" in RETURN)
	assert ("name" in RETURN ["brand"])
	assert (type (RETURN ["brand"]["name"]) == str)
	
	assert (
		RETURN ["defined"] ==
		{
			"serving size": {
				"quantity": 3
			}
		}
	)
	assert (
		RETURN ["form"] ==
		{
			"unit": "Tablet",
			"quantity": 90
		}
	)
	

	
	EQ.CHECK (len (RETURN ["ingredients"]["quantified list"]), 9)

	EQ.CHECK (
		RETURN ["ingredients"]["quantified list"][7]["name"],
		"Vitamin D3"
	)
	EQ.CHECK (
		RETURN ["ingredients"]["quantified list"][7]["quantity per form"],
		{
			"form": "Tablet",
			"amount": "20/3",
			"unit": "mcg"
		}
	)
	EQ.CHECK (
		RETURN ["ingredients"]["quantified list"][7]["quantity per form, in grams"],
		{
			"form": "Tablet",
			"amount": "1/150000",
			"unit": "g"
		}
	)
	EQ.CHECK (
		RETURN ["ingredients"]["quantified list"][7]["quantity per package, in grams"],
		{
			"amount": "3/5000",
				"unit": "g"
		}
	)

	
	assert (len (RETURN ["ingredients"]["unquantified"]) == 4)

	EQ.CHECK (
		RETURN ["mass of quantified ingredients"]["caculated per package, ignoring IU, RAE, DFE, in grams"],
		"580153/375000"
	)
	EQ.CHECK (
		RETURN ["mass of quantified ingredients"]["caculated per form, ignoring IU, RAE, DFE in grams"],
		"580153/33750000"
	)

	
	
CHECKS = {
	"CALCIUM 261967": CHECK_1
}