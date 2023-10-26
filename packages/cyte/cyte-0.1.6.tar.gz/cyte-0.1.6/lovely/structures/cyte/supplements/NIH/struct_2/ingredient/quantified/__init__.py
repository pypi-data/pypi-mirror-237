





from fractions import Fraction

import cyte.mass.SWAP as mass_SWAP
import cyte.supplements.NIH.struct_2.ingredient.quantified.per.package as ingredient_quantified_per_package 
import cyte.supplements.NIH.struct_2.ingredient.quantified.per.form as ingredient_quantified_per_form

import json

def calc (
	ingredient, 
	NIH_supplement_data_struct_2
):
	quantity_of_form_per_package = NIH_supplement_data_struct_2 ["form"]["quantity"]

	form = NIH_supplement_data_struct_2 ["form"];
	ingredient_serving_size_quantity = ingredient ["quantity"][0]["servingSizeQuantity"]

	assert ("name" in ingredient)
	name = ingredient ["name"]

	'''
	#
	#	make sure that the serving size quantity of the package
	#	is the same as the serving size quantity of the ingredient 
	#
	equal_serving_sizes = (
		ingredient_serving_size_quantity == 
		defined ["serving size"]["quantity"]
	)

	
	#
	#	if the form is pills, tablets, etc.
	#	then, make sure that:
	#		
	#		total quantity / ingredient serving size quantity = an integer
	#
	if (form ["unit"] not in [ "gram" ]):
		assert (
			Fraction (
				form ["quantity"], 
				ingredient_serving_size_quantity
			).denominator == 1,
		)

	
	
	#
	#	per form calculations
	#
	ingredient_unit = ingredient ["quantity"][0]["unit"]

	#
	#	ingredient amount per form = ingredient quantity / serving size quantity
	#
	ingredient_amount_per_form = ""
	if (
		len (ingredient ["quantity"]) == 1 and
		equal_serving_sizes
	):	
		ingredient_amount_per_form = Fraction (
			Fraction (ingredient ["quantity"][0]["quantity"]),
			Fraction (defined ["serving size"]["quantity"])
		)
		
	else:
		raise Exception ("Ingredient amount could not be calculated.")

	try:
		ingredient_amount_per_form_float_string = str (float (ingredient_amount_per_form))
	except Exception as E:
		ingredient_amount_per_form_float = "?"
	
	try:	
		fraction_per_form_in_grams = Fraction (mass_SWAP.START ([ 
			ingredient_amount_per_form, 
			ingredient_unit 
		], "grams"))
		
		print ("fraction_per_form_in_grams:", name, fraction_per_form_in_grams)
		
	except Exception as E:
		fraction_per_form_in_grams = "?"
	
	try:
		float_per_form_in_grams = float (fraction_per_form_in_grams)
	except Exception as E:
		float_per_form_in_grams = "?"
	'''

	[
		ingredient_unit,
		
		ingredient_amount_per_form,
		ingredient_amount_per_form_float_string,
		
		fraction_per_form_in_grams,
		float_per_form_in_grams
	] = ingredient_quantified_per_form.calc (
		NIH_supplement_data_struct_2,
		ingredient
	) 
		
	print (ingredient["name"], [
		ingredient_unit,
		
		ingredient_amount_per_form,
		ingredient_amount_per_form_float_string,
		
		fraction_per_form_in_grams,
		float_per_form_in_grams
	])
		
	[ 
		fraction_per_package_in_grams,
		float_per_package_in_grams
	] = ingredient_quantified_per_package.calc (
		fraction_per_form_in_grams,
		quantity_of_form_per_package
	)
	
	#
	#	per serving calculations
	#	
	

	return {
		"name": name,
		
		"mass": {
			"per package": {
				#
				# "fraction string grams": "97383/50000"
				#
				"fraction string grams": str (fraction_per_package_in_grams),
				"float string grams": str (float_per_package_in_grams),
				"listed": {
					"unit": ingredient_unit
				}
			},
			"per form": {
				"fraction string grams": str (fraction_per_form_in_grams),
				"float string grams": str (float_per_form_in_grams),
				"listed": {
					"unit": ingredient_unit,
					"fraction string": str (ingredient_amount_per_form),
					"float string": ingredient_amount_per_form_float_string
				}
			},
			"per serving": {}
		},
		
		"quantity per form": {
			"form": form ["unit"],
			"amount": str (ingredient_amount_per_form),
			"unit": ingredient_unit
		},
		"quantity per form, in grams": {
			"form": form ["unit"],
			"amount": str (fraction_per_form_in_grams),
			"unit": "g"
		},
		"quantity per package, in grams": {
			"amount": str (fraction_per_package_in_grams),
			"unit": "g"
		},
	}

