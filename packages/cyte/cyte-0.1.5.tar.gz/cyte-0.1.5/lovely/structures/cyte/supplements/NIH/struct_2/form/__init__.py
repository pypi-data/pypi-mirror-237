




def CALC_QUANTITY (NIH_SUPPLEMENT_DATA):
	assert ("netContents" in NIH_SUPPLEMENT_DATA)
	NET_CONTENTS = NIH_SUPPLEMENT_DATA ["netContents"]
	
	if (
		len (NET_CONTENTS) == 1
	):
		return NET_CONTENTS [0] ["quantity"]
		
	raise Exception ("The form quantity of the supplement could not be calculated.")
