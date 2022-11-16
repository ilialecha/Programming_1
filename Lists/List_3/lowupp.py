def lowupp(s):
	'''
	>>> lowupp('_Hi There!')
	'hi there!'
	>>> lowupp('^Hi There!')
	'HI THERE!'
	>>> lowupp('Hi There!')
	'Hi There!'
	'''
	
	
	return s[1:].lower() if s.startswith('_') else s[1:].upper() if s.startswith("^") else s
	
	
	'''
	if s.startswith('_'):
		
		return s.lower()[1:]
		
	elif s.startswith("^"):
		
		return s.upper()[1:]
		
	else: 
		return s
	'''


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
