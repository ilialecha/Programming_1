def count_a(s, sc):
	'''
	>>> count_a('naturally', 'u')
	1
	>>> count_a('russian', 't')
	-1
	>>> count_a('adaptation', 'a')
	0
	>>> count_a('adaptation', 'n')
	3
	'''
	count = 0 

	if sc == s[0]:
		return 0
		
	elif sc not in s:
		return -1
	
	new_string = s[0:s.index(sc)]
	
	for i in new_string:
		if i == 'a':
			count += 1
	
	return count


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
