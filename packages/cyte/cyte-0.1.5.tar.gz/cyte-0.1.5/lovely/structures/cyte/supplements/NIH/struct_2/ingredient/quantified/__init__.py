


'''
	Vitamin A:
		https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/
		
		1 mcg RAE == either (
			1 mcg retinol, 
			2 mcg supplemental beta-carotene, 
			12 mcg dietary beta-carotene, 
			or 24 mcg dietary alpha-carotene or beta-cryptoxanthin
		)
		
		RAE is how much retinol the body produces (on average) with 
		each of the equivalents.
		
		Vitamin A1 == Retinol
'''

'''
	FOLATE:
		https://ods.od.nih.gov/factsheets/Folate-HealthProfessional/
		
		DFE == dietary folate equivalents
		
		1 mcg DFE = either (
			1 mcg food folate
			0.6 mcg folic acid from fortified foods or dietary supplements consumed with foods
			0.5 mcg folic acid from dietary supplements taken on an empty stomach
		)
'''


from fractions import Fraction

import cyte.mass.SWAP as mass_SWAP

def calc (
	ingredient, 
	RETURN
):
	DEFINED = RETURN ["defined"];
	FORM = RETURN ["form"];

	QUANTITY_OF_FORM_PER_PACKAGE = RETURN ["form"]["quantity"]

	assert ("name" in ingredient)
	NAME = ingredient ["name"]

	AMOUNT = ""
	if (
		len (ingredient ["quantity"]) == 1 and
		ingredient ["quantity"][0]["servingSizeQuantity"] == DEFINED ["serving size"]["quantity"] and
		Fraction (
			FORM ["quantity"], 
			ingredient ["quantity"][0]["servingSizeQuantity"]
		).denominator == 1
	):
		print (
			ingredient ["quantity"][0]["quantity"],
			DEFINED ["serving size"]["quantity"]
		)
	
		AMOUNT = Fraction (
			Fraction (ingredient ["quantity"][0]["quantity"]),
			Fraction (DEFINED ["serving size"]["quantity"])
		)
		
	else:
		raise Exception ("Ingredient amount could not be calculated.")


	UNIT = ingredient ["quantity"][0]["unit"]

	
	try:
		QUANTITY_PER_FORM_IN_GRAMS = str (mass_SWAP.START ([ AMOUNT, UNIT ], "grams"))
	except Exception as E:
		QUANTITY_PER_FORM_IN_GRAMS = "?"
	
	
	try:
		QUANTITY_PER_PACKAGE_IN_GRAMS = str (Fraction (QUANTITY_PER_FORM_IN_GRAMS) * Fraction (QUANTITY_OF_FORM_PER_PACKAGE))
	except Exception as E:
		QUANTITY_PER_PACKAGE_IN_GRAMS = "?"
	

	return {
		"name": NAME,
		
		"quantity per form": {
			"form": FORM ["unit"],
			"amount": str (AMOUNT),
			"unit": UNIT
		},
		"quantity per form, in grams": {
			"form": FORM ["unit"],
			"amount": QUANTITY_PER_FORM_IN_GRAMS,
			"unit": "g"
		},
		"quantity per package, in grams": {
			"amount": QUANTITY_PER_PACKAGE_IN_GRAMS,
			"unit": "g"
		},
	}

