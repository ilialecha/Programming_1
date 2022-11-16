def multiple_in_interval(a,b,x):
	'''
	>>> multiple_in_interval(5, 10, 2)
	True
	>>> multiple_in_interval(10, 5, 2)
	False
	>>> multiple_in_interval(10, 10, 2)
	True
	>>> multiple_in_interval(51, 58, 5)
	True
	>>> multiple_in_interval(50, 55, 7)
	False
	>>> multiple_in_interval(100, 180, 92)
	False
	>>> multiple_in_interval(5, 10, 2) and (3>2)
	True
	'''
	
	for i in range(a,b+1):
		#multx = i%x
		if i % x == 0: # Si multx == 0 el numero es multiplo
			return True
	return False
	
	
	
	'''
	for number in range(a, b+1):
		if number % x == 0:
			return True
	return False
	'''
	
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
	
	
multiple_in_interval(5, 10, 2)
	
	

