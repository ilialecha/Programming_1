#y = [2*a for a in x if a % 2 == 1]
def cap_let_counter(s):
	'''
	>>> cap_let_counter('Game Over')
	2
	>>> cap_let_counter('Add: 3 + 5')
	1
	>>> cap_let_counter('000MONTsERRAT000')
	9
	'''
	
	return sum([1 for let in s if let.isupper()])

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
