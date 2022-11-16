def low_let_counter(s):
	'''
	>>> low_let_counter('The End')
	4
	>>> low_let_counter('Compute: 3 + 5')
	6
	>>> low_let_counter('66sixty_six66')
	8
	'''
	
	return (sum([1 for let in s if let.isalpha() and  let.islower()]))
	


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

