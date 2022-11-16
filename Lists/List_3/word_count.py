def word_count(string):
	'''
	>>> word_count('Qui invenit amicum invenit thesaurum')
	5
	>>> word_count('alea iacta          est')
	3
	>>> word_count('KingKong')
	1
	>>> word_count(' by' )
	1
	>>> word_count('by' )
	1
	>>> word_count(' by with 	this I mean, mdfk')
	6
	
	'''
	
	total_words = 1
	index = 0
	
	
	if not " " in string:
		return 1
		
	for i in string:
		
		if index == 0 and i == " ":
			continue
			
		if i == " " and string[index-1] != " ":
			total_words += 1
		
		index += 1	
		
	return total_words


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

