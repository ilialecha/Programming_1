def regroup(s):
	'''
	>>> regroup('r2b2')
	'rb22'
	>>> regroup('a45tr09pw')
	'atrpw4509'
	>>> regroup('nonumbers')
	'nonumbers'
	>>> regroup('543210')
	'543210'
	'''
	letters = ''
	numbers = ''

	for i in s:
		if i.isdigit():
			numbers += i
		else:
			letters += i
	
	return letters+numbers
		
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
