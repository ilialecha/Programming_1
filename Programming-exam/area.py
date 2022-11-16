import math
def area(t,a,b):
	'''
	>>> area('rectangle', 3.1, 4.0)
	12.4
	>>> area('triangle', 6.0, 2.0)
	6.0
	>>> area('rectangle', 8.2, 8.2)
	67.24
	>>> area('circle', 1.0, 0.0)
	3.141592653589793
	'''
	if t == "rectangle":
		return a*b
	elif t == "triangle":
		return (a*b)/2
	elif t == "circle":
		return math.pi *(a*a)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
