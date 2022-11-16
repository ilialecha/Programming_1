import math
def walker(x, y, steps):
	'''
	>>> walker(4, 1, 'NEENWNWWS')
	(3, 3)
	>>> walker(3, 5, 'NESW')
	(3, 5)
	>>> walker(0, 4, 'SSSSEWEWNNNN')
	(0, 4)
	>>> walker(0, 0, 'SWSWNES')
	(-1, -2)
	>>> walker(6, 3, '')
	(6, 3)
	'''

	for step in steps:
		if step == "N":
			y+=1
		elif step == "S":
			y-=1
		elif step == "E":
			x+=1
		elif step == "W":
			x-=1
	
	return (x,y)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
