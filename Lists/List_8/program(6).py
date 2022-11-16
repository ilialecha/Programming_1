def next_word_list(w, f):
	'''
	>>> next_word_list('red', ['red','yellow','red','black','grey','red'])
	['yellow', 'black']
	>>> next_word_list('big', ['small','big'])
	[]
	>>> next_word_list('big' , ['big','small'])
	['small']
	>>> next_word_list('blue', ['green'])
	[]
	>>> next_word_list('blue', [])
	[]
	>>> next_word_list('red', ['red','red','red'])
	['red', 'red']
	'''
	idx = []
	nw = False
	for i, n in enumerate(f):
		if nw:
			idx.append(i)
			nw = False

		if n == w:
			nw = True


	a = []
	for n in idx:
		a.append(f[n])
	
	return a

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose = True)
