def grade(s):
	'''
	>>> grade(4.99)
	'suspens'
	>>> grade(8)
	'notable'
	>>> grade(6.99)
	'aprovat'
	>>> grade(9.5)
	'excel.lent'
	>>> grade(10)
	'MH'
	'''
	if 0<=s<=4.99:
		return 'suspens'
		
	elif 5.00<=s<=6.99:
		return 'aprovat'
		
	elif 7.00<=s<=8.99:
		return 'notable'
		
	elif 9.00<=s<10.0:
		return 'excel.lent'
		
	elif s==10.0:
		return 'MH'

	

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
