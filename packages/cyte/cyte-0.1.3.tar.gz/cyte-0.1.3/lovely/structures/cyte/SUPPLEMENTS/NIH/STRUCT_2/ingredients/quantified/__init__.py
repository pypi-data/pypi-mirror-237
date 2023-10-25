
import cyte.SUPPLEMENTS.NIH.STRUCT_2.ingredients.quantified.ingredient as quantified_ingredient 


def CALC (
	NIH_SUPPLEMENT_DATA,
	RETURN
):
	assert ("ingredientRows" in NIH_SUPPLEMENT_DATA)
	
	INGREDIENTS = []
	
	INGREDIENT_ROWS = NIH_SUPPLEMENT_DATA ["ingredientRows"]
	for INGREDIENT in INGREDIENT_ROWS:
		INGREDIENTS.append (
			quantified_ingredient.calc (INGREDIENT, RETURN)
		)

		
	INGREDIENTS.sort (
		key = lambda INGREDIENT : INGREDIENT ["name"]
	)

	return INGREDIENTS