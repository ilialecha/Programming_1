def check_personal(n, a, e):
	'''
	>>> check_personal("Maria", 22, True)
	True
	>>> check_personal("Joan", 19, False)
	False
	>>> check_personal("Miquel", 20, False)
	True
	>>> check_personal("Josep", 21, True)
	True
	>>> check_personal("Jaume", 18, True)
	False
	>>> check_personal("Julieta", 23, False)
	False
	'''
	
	return a >= 20 and (n[0] == 'M' or e)
	

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
