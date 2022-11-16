def sum_interval(a, b):
	'''
	>>> sum_interval(5,10)
	45
	>>> sum_interval(1,100)
	5050
	>>> sum_interval(10,20)
	165
	'''
	
	total = 0
	
	for i in range(a,b+1):
			total += i
	
	return total		

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
