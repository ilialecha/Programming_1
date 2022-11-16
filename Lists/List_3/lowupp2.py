def lowupp(s):

	'''
	>>> lowupp('_Hi There!')
	'hi there!'
	>>> lowupp('^Hi There!')
	'HI THERE!'
	>>> lowupp('Hi There!')
	'Hi There!'
	>>> lowupp('')
	''
	'''
	if len(s)>0:
		return s.lower()[1:] if (s[0] == '_') else s.upper()[1:] if (s[0] == "^") else s
	else:
		return ''




# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
