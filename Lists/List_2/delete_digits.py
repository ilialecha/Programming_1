
def delete_digits(s):
	'''
	>>> delete_digits('#Pelham 1-2-3#')
	'#Pelham --#'
	>>> delete_digits('7 up')
	' up'
	>>> delete_digits('92920')
	''
	'''
	newString = ''
	
	for i in s:
		
		if not i in '1234567890':
			newString += i
		
	return newString

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

