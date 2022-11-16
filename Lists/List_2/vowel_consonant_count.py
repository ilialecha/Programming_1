
def vowel_consonant_count(s):
	'''
	>>> vowel_consonant_count('SpartacUs')
	(3, 6)
	>>> vowel_consonant_count('KingKong')
	(2, 6)
	'''
	tv = 0
	tc = 0

	
	for i in s.lower():
		if i in 'aeiou':
			tv += 1
		else:
			tc += 1
	return tv, tc
	
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)


