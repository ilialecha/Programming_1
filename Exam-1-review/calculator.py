def calculator(a,b,operator):
	'''
	>>> calculator(3.2, 5, '+')
	8.2
	>>> calculator(2, 3 + 1/2, '-')
	-1.5
	>>> calculator(1/2, 4, '*') - calculator(1, 1, '+')
	0.0
	'''
	if operator == '+':
		return a + b
	elif operator == '-':
		return a - b
	elif operator == '*':
		return a*b

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)


