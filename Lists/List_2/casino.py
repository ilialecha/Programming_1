def buy_tokens(n):
	'''
	>>> buy_tokens(20)
	(0, 5)
	>>> buy_tokens(50)
	(6, 2)
	>>> buy_tokens(39)
	(5, 1)
	'''
	
	'''Fichas rojas iniciales'''
	number_red = n//7

	'''Sobrante de las fichas rojas'''
	rest = n%7
	
	'''Mientras el restante de las fichas rojas NO sea divisible entre 4:'''
	while rest % 4 != 0:
		'''Restamos 1 ficha roja'''
		number_red -= 1
		
		'''Al haber restado una ficha roja, sumamos el valor de una (7 euros) al resto'''
		rest += 7 
	
	
	return number_red, rest//4

		
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
