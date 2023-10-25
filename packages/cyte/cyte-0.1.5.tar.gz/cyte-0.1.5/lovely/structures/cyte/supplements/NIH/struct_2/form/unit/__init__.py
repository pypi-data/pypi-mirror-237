




def calc (nih_supplement_data):
	assert ("netContents" in nih_supplement_data)
	NET_CONTENTS = nih_supplement_data ["netContents"]

	assert ("physicalState" in nih_supplement_data)
	PHYSICAL_STATE = nih_supplement_data ["physicalState"]

	assert ("servingSizes" in nih_supplement_data)
	SERVING_SIZES = nih_supplement_data ["servingSizes"]

	if (
		len (NET_CONTENTS) == 1 and
		NET_CONTENTS [0] ["unit"] == "Tablet(s)" and 
		PHYSICAL_STATE ["langualCodeDescription"] == "Tablet or Pill" and
		len (SERVING_SIZES) == 1 and
		SERVING_SIZES [0] ["unit"] == "Tablet(s)"
	):
		return "Tablet"
		
	if (
		len (NET_CONTENTS) == 1 and
		NET_CONTENTS [0] ["unit"] == "Coated Tablet(s)" and 
		PHYSICAL_STATE ["langualCodeDescription"] == "Tablet or Pill" and
		len (SERVING_SIZES) == 1 and
		SERVING_SIZES [0] ["unit"] == "Tablet(s)"
	):
		return "Coated Tablet"
		
	raise Exception ("The form unit of the supplement could not be calculated.")