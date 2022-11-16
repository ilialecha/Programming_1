def kth_word(s, k):
	'''
	>>> kth_word('Alea iacta est', 3)
	'est'
	>>> kth_word('Alea iacta est', 1)
	'Alea'
	>>> kth_word('KingKong', 2)
	''
	'''
	
	prev = ' '
	count = 0 
	for x in s:
		if x!= ' ' and prev==' ': #New word
			count += 1
			word = x
			
		elif x!= ' ' and prev != ' ': #Word continues
			
			word += x

		
		elif x==' ' and prev!=' ': #Word finishes
			
			if count==k:
				return word
				
		prev = x

	if count == k:
		return word
	else:
		return ''

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
