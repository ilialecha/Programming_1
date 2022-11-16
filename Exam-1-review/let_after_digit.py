def let_after_digit(s):
	'''
	>>> let_after_digit('Game Over')
	(False, '#')
	>>> let_after_digit('Error 324:---Identifier not defined---')
	(True, 'I')
	>>> let_after_digit('xRs123')
	(False, '#')
	>>> let_after_digit('1@#$X2Y')
	(True, 'X')
	'''
	
	digit_found = False
	
	for char in s:
		if char.isdigit() and not digit_found:
			digit_found = True
		
		if digit_found and char.isalpha():
			return (True, char)

	return (False, "#")

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
