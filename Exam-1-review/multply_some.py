def multiply_some(n, a, b):
	'''
	>>> multiply_some(2, 5, 10)
	480
	>>> multiply_some(3, 10, 20)
	3240
	>>> multiply_some(5, 54, 57)
	55
	>>> multiply_some(8, 19, 23)
	1
	'''
	
	result = 1

	if n < a <= b:
		for number in range(a, b+1):
			#print(str(number)+" % "+str(n)+" = "+ str(number%n))
			if number%n == 0:
				result *= number

		return result
	
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

