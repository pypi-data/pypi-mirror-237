

'''
import cyte.structs.scan.TREES.SORT as SORT_TREES
SORT_TREES.START (TREES)
'''

def START (TREES):
	TREES.sort (key = lambda struct : struct ["names"][0])

	return