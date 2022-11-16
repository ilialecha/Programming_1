def intersection(a, b, c, d):
	'''
	>>> intersection(1, 5, 3, 7)
	(3, 5)
	>>> intersection(10, 16, 12, 15)
	(12, 15)
	>>> intersection(3, 5, 2, 11)
	(3, 5)
	>>> intersection(1, 4, 4, 6)
	(4, 4)
	'''
	if a <= c and d <= b:
		p = c
		q = d
	elif c <= a and b <= d:
		p = a
		q = b
	elif a <= c and c <= b:
		p = c
		q = b
	else:
		p = a
		q = d

	return p, q


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
