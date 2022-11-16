def leading_hand(h, m):
	'''
	>>> leading_hand(22, 51)
	'minute hand'
	>>> leading_hand(21, 45)
	'draw'
	>>> leading_hand(6, 28)
	'hour hand'
	>>> leading_hand(4, 20)
	'draw'
	'''
	
	'''
		Compruebo que los parametros esten entre los valores deseados.
	'''
	if (0 <= h < 24) & (0 <= m < 60):
		
		
		'''
		Por si nos pasan una hora en formato 24h  Ej. 23%12 = 11
		'''
		h = h%12
		
		'''
		Creamos variable resultado y le asignamos un String vacio para posterior uso.
		'''
		result = ""
		
		if (h * 5) == m: 
			result = 'draw'
		elif (h * 5) < m: 
			result = 'minute hand'
		else:
			result = 'hour hand'
		
		return result

	

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
