def decompose(n):
	'''
	>>>decompose(147)
	(0, 2, 27)
	'''
	s = n % 60
	
	m = n // 60
	
	h = m // 60
	
	m = m % 60
	
	return h, m, s	


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
