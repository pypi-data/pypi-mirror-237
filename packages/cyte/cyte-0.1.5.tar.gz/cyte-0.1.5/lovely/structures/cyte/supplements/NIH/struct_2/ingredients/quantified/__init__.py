
import cyte.supplements.NIH.struct_2.ingredient.quantified as quantified_ingredient 


def CALC (
	NIH_supplement_data,
	NIH_supplement_data_struct_2
):
	assert ("ingredientRows" in NIH_supplement_data)
	
	ingredients = []
	
	ingrdient_rows = NIH_supplement_data ["ingredientRows"]
	for ingredient in ingrdient_rows:
		quantified = quantified_ingredient.calc (
			ingredient, 
			NIH_supplement_data_struct_2
		)
		
		ingredients.append (quantified)

	ingredients.sort (
		key = lambda INGREDIENT : INGREDIENT ["name"]
	)

	return ingredients