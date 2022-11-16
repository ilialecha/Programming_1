def is_power7(n):
    if n == 0:
        return False
    while n != 1:
        if n%7 != 0:
            return False
        n = n//7
    return True

def short_power7_chains(f, k):
	'''
	>>> short_power7_chains([1, 7, 49, 7*7*7, 2], 3)
	False
	>>> short_power7_chains([1, 7, 49, 7*7*7, 2], 4)
	True
	>>> short_power7_chains([1, 7, 14, 7*7*7, 21, 28], 2)
	True
	>>> short_power7_chains([14, 7], 1)
	True
	>>> short_power7_chains([], 1)
	True
	'''
	c = 0
	for s in f:
		if is_power7(s) and c < k:
			c += 1
		elif not is_power7(s):
			c = 0
		else:
			return False
	return True
	
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose = True)
