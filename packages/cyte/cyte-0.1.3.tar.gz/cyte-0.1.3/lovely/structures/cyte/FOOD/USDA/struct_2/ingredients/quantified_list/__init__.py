

'''


'''
import cyte.FOOD.USDA.struct_2.ingredients.quantified_list.ingredient as QUANTIFIED_INGREDIENT

def calc (
	usda_food_data, 
	usda_food_data_CALCULATED
):
	INGREDIENTS = []

	assert ("foodNutrients" in usda_food_data)
	FOOD_NUTRIENTS = usda_food_data ["foodNutrients"]
	for FOOD_NUTRIENT in FOOD_NUTRIENTS:
		quantified = QUANTIFIED_INGREDIENT.CALC (
			FOOD_NUTRIENT,
			usda_food_data_CALCULATED
		)
		
		if (quantified != "energy"):
			INGREDIENTS.append (quantified)
	

	return INGREDIENTS