
'''
	python3 STATUS.py "structs/scan/NAMES/contains_substring/STATUS_DYNAMIC_1.py"
'''

import cyte.structs.DB.access as access
import cyte.structs.scan.NAMES.contains_substring as structs_WHERE_NAME_CONTAINS_SUBSTRING

def CHECK_1 ():	
	structs = structs_WHERE_NAME_CONTAINS_SUBSTRING.FIND (
		access.DB (),
		"VITAMIN B"
	)
	structs_VAR_CAPS = structs_WHERE_NAME_CONTAINS_SUBSTRING.FIND (
		access.DB (),
		"VItAmIn B"
	)
	structs_LOWER = structs_WHERE_NAME_CONTAINS_SUBSTRING.FIND (
		access.DB (),
		"vitamin b"
	)

	for STRUCT in structs:
		print (STRUCT)

	assert (len (structs) >= 6);

	assert (len (structs) == len (structs_VAR_CAPS))
	assert (len (structs) == len (structs_LOWER))

	return;
	
def CHECK_2 ():	
	structs = structs_WHERE_NAME_CONTAINS_SUBSTRING.FIND (access.DB (), "Magnesium")
	
	REGIONS = []
	for STRUCT in structs:
		print (STRUCT)
		REGIONS.append (STRUCT ["region"])

	assert (len (structs) >= 1);
	assert (30 in REGIONS);


	return;
	
CHECKS = {
	"Structs have a name that contains 'vitamin b'": CHECK_1,
	"Struct has a name that contains 'Magnesium'": CHECK_2
}