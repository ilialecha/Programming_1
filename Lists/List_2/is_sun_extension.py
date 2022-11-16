def is_sun_extension(s):
	'''
	>>> is_sun_extension('sun')
	True
	>>> is_sun_extension('assumption')
	True
	>>> is_sun_extension('assume')
	False
	>>> is_sun_extension('russian')
	False
	>>> is_sun_extension('scouting')
	True
	>>> is_sun_extension('innocuous')
	False
	'''

	wanted = 's'
	found = False
	
	'''
	for i in s:
		
		#Si la letra es igual a wanted y wanted == s  --> Pasamos a buscar wanted = 'u'
		if wanted == 's' and i == wanted:
			wanted = 'u'
		
		#Si la letra es igual a wanted y wanted == u  --> Pasamos a buscar wanted = 'n'
		elif wanted == 'u' and i == wanted :
				wanted = 'n'
		
		#Si la letra es igual a wanted y wanted == n  --> Quiere decir que está la palabra SUN. 
		elif wanted == 'n' and i == wanted:
			return True		
	return False
	'''
	
	for i in s:
		if i == wanted:
			if wanted == 's':
				wanted = 'u'
			elif wanted == 'u':
				wanted = 'n'
			elif wanted == 'n':
				found = True
	
	
	return found
	
	
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)



