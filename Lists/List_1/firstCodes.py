def parab(x):
	'''
	Evaluates on integer x parabola x^2 -3x + 2
	>>> parab(0)
	2
	>>> parab(2)
	0
	'''
	# the function computation remains the same
	return x*x - 3*x + 2

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)


print("RESULTS FOR PARAB FUNCTION :")
print("parab(5) = \t\t\t", parab(5))
print("parab(3.2) = \t\t\t", parab(3.2))
print("parab(4) + parab(2.1) - 3.3 = \t", parab(4) + parab(2.1) - 3.3)
print("max(parab(5)-1, parab(3)+2) = \t", max(parab(5)-1, parab(3)+2))
