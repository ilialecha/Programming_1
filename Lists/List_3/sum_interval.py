def sum_interval(a, b, n):
	'''
	>>> sum_interval(5,10,8)
	8
	>>> sum_interval(5,10,3)
	0
	>>> sum_interval(1,100,6)
	510
	>>> sum_interval(10,20,0)
	30
	'''
	
	total = 0
	
	for i in range(a,b+1):
		
		if i%10 == n: 
			total += i
	
	return total		

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
