def inclusion(x1, y1, x2, y2):
	'''
	>>> inclusion(6,3,4,2)
	second inside first
	>>> inclusion(3,6,4,2)
	second inside first
	>>> inclusion(6,3,7,2)
	none
	>>> inclusion(4,2,3,6)
	first inside second
	'''
	result = 'none'
	if  x1*2 + y1*2 < x2*2 + y2*2:
		result = "first inside second"
	elif x1*2 + y1*2 > x2*2 + y2*2:
		result = "second inside first"
	
	return print(result)
	
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)



