def slow_pi_approx(a):
	'''
	>>> slow_pi_approx(10)
	3.2323
	>>> slow_pi_approx(100)
	3.1515
	>>> slow_pi_approx(1000)
	3.1426
	'''

	total = 0

	for i in range(0,a+1):
		total += (((-1)**i) / (2*i+1))
		
	return round(total * 4.0, 4)

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
