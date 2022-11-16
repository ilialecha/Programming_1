def is_univariate_word(s):
	
	'''
	>>> is_univariate_word('xxXxxxXX')
	True
	>>> is_univariate_word('xyyyyYYY')
	False
	>>> is_univariate_word('y')
	True
	>>> is_univariate_word('yyyyx')
	False
	'''
	
	firstLetter = s.lower()[0]
	
	for i in s.lower():
		if i != firstLetter:
			return False
			
	return True
	
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)



