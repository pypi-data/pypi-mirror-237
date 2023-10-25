


'''
	"mass of quantified ingredients": {
		"caculated per package, ignoring IU": {
			
		}
	}
'''

from fractions import Fraction

def CALC (NIH_SUPPLEMENT_DATA, RETURN):
	QUANTITY_OF_FORM = RETURN ["form"]["quantity"]
	QUANTIFIED_INGREDIENTS = RETURN ["ingredients"]["quantified grove"]
	
	QUANTITY_IN_GRAMS = 0
	
	skipped = []
	
	for INGREDIENT in QUANTIFIED_INGREDIENTS:
		AMOUNT = INGREDIENT [
			"quantity per form, in grams"
		]["amount"];
		if (AMOUNT == "?"):
			skipped.append (INGREDIENT ["name"])
			
		else:
			QUANTITY_IN_GRAMS += Fraction (INGREDIENT [
				"quantity per form, in grams"
			]["amount"])
		
	#print ("QUANTITY_OF_FORM:", QUANTITY_OF_FORM)	
	
	print ("skipped:", skipped)
	
	return {
		"sum of quantified ingredients per package, exluding effectual": {
			"grams": str (QUANTITY_IN_GRAMS)
		},
		"sum of quantified ingredients per form, exluding effectual": {
			"grams": str (Fraction (QUANTITY_IN_GRAMS, QUANTITY_OF_FORM)),
		}
	}
	
	"""	
		"caculated per package, ignoring IU, RAE, DFE, in grams": str (QUANTITY_IN_GRAMS),
		"caculated per form, ignoring IU, RAE, DFE in grams": str (Fraction (QUANTITY_IN_GRAMS, QUANTITY_OF_FORM)),
		"skipped": SKIPPED
	"""