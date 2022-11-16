def update_arrival(h, m, d):
	'''
	>>> update_arrival(10, 45, 20)
	(11, 5)
	>>> update_arrival(12, 30, 60)
	(13, 30)
	>>> update_arrival(22, 0, 120)
	(0, 0)
	>>> update_arrival(23, 57, 5 + 24*60)
	(0, 2)
	'''
	
	initTime = h * 60 + m
	
	arrivalTime = initTime + d
	
	new_m =  arrivalTime % 60
	
	new_h = (arrivalTime//60) % 24

	return new_h, new_m


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
