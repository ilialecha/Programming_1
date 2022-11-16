def evaluator(op, p,q):
	'''
	>>> evaluator('or', False, True)
	True
	>>> evaluator('or', 1 == 5, False)
	False
	>>> evaluator('and', True,  2 == 3) or evaluator('and', True, False)
	False
	>>> evaluator('not_or', 1 == 5, False)
	True
	'''
	#More efficient way
	return (p or q) if  op == 'or' else (p and q) if op == 'and' else (not(p or q)) 
	
	#No that efficient
	'''
	if op == "or":
		return p or q
	elif op == "and":
		return p and q
	elif op == 'not_or':
		return not (p or q)
	'''
	

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
