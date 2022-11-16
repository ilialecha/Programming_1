def winner(p,q,r,s):	
	'''
	>>> winner(1, 3, 5, 3)
	1
	>>> winner(2, 4, 4, 3)
	2
	>>> winner(1, 3, 2, 3)
	2
	>>> winner(2, 4, 3, 3)
	0
	>>> winner(4, 4, 5, 6)
	0
	'''
	
	p1 = p + q 
	
	p2 = r + s
	
	if p1 > p2 and p1<=7 or (p2>7 and p1<=7):
		return 1
	elif p2 > p1 and p2<=7 or (p1>7 and p2<=7):
		return 2 
	else:
		return 0
	
		


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
