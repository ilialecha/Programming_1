def add_one_day(d, m, y):
	'''
	>>> add_one_day(12, 3, 2002)
	(13, 3, 2002)
	>>> add_one_day(30, 6, 1975)
	(1, 7, 1975)
	>>> add_one_day(28, 2, 2017)
	(1, 3, 2017)
	>>> add_one_day(15, 6, 1975)[0]
	16
	>>> add_one_day(31, 12, 2017)
	(1, 1, 2018)
	'''
	
	d += 1		
	if  d > 31 and m in [1,3,5,7,8,10,12]: 
		d = 1
		m += 1
		if m > 12:
			m = 1 
			y +=1
			
	elif  d > 30 and m in [4,6,9,11]: 
		d = 1
		m += 1
		if m > 12:
			m = 1 
			y +=1
			
	elif d > 28 and m == 2:
		d = 1
		m+= 1
		if m > 12:
			m = 1
			y+=1

	return (d, m, y)
		
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
