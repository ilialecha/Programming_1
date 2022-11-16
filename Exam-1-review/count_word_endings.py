def count_word_endings(x):
	'''
	>>> count_word_endings( ('dog', 'cat', 'birds', 'reached', 'eat') )
	(1, 1, 2)
	>>> count_word_endings( ('dog', 'had', 'cat', 'reached') )
	(0, 2, 1)
	>>> count_word_endings( ('dog', 'fog', 'why', 'not') )
	(0, 0, 1)
	>>> sum( count_word_endings( ('dog', 'had', 'cat', 'reached') ) )
	3
	'''
	
	s_term_auto = sum((1 for word in x if word[-1]=='s'))
	
	d_term_auto = sum((1 for word in x if word[-1]=='d'))
	
	t_term_auto = sum((1 for word in x if word[-1]=='t'))
	
	return (s_term_auto, d_term_auto, t_term_auto)
	
	
	'''
	s_term = 0
	d_term = 0
	t_term = 0
	
	for word in x:
		if word[-1] == "s":
			s_term += 1
		elif word[-1] == "d":
			d_term += 1
		elif word[-1] == "t":
			t_term += 1
	return (s_term, d_term, t_term)
	'''

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

count_word_endings( ('dog', 'cat', 'birds', 'reached', 'eat'))
