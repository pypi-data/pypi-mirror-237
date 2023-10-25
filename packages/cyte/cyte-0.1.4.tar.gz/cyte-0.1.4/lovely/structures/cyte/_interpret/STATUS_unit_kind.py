



'''
	python3 status.py "_interpret/STATUS_unit_kind.py"
'''

import cyte._interpret.unit_kind as UNIT_KIND

from fractions import Fraction

def CHECK_1 ():
	assert (UNIT_KIND.CALC ("ml") == "volume")
	assert (UNIT_KIND.CALC ("fl oz") == "volume")
	
	assert (UNIT_KIND.CALC ("GRAM") == "mass")
	assert (UNIT_KIND.CALC ("gram") == "mass")
	
	assert (UNIT_KIND.CALC ("IU") == "effectual mass")

	assert (UNIT_KIND.CALC ("kcal") == "energy")


CHECKS = {
	"CHECK 1": CHECK_1
}
	


