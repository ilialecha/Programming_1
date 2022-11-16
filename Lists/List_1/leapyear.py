
def leapyear(y):
	'''
	>>> leapyear(1999)
	False
	>>> leapyear(1968)
	True
	>>> leapyear(2000)
	True
	>>> leapyear(1800)
	False
	'''

	#if y % 4 == 0:
		
	#	if y % 100 == 0:
	#		if y % 400 == 0:
	#			return True # Divisor entre 4, 100 y 400
	#		else:
	#			return False # Divisor entre 4 y 100 pero no 400
	#	else:
	#		return True # Divisor entre 4 pero no entre 100
	#
	#else:
	#	return False
		
		
	
	return (y%4 == 0 ) and (y%100 != 0 or y%400==0)	

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
