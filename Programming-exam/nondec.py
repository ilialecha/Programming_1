def nondec(n):
	'''
	>>> nondec(113355779)
	True
	>>> nondec(44569)
	True
	>>> nondec(346234)
	False
	>>> nondec(222)
	True
	'''
	
	n_str = str(n)
	aux_digit = n_str[0]

	
	for digit in n_str[1:]:
		if not int(digit) >= int(aux_digit):
			return False
		aux_digit = digit
	return True
	

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

