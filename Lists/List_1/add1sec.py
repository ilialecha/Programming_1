def add1sec(h, m, s):
	'''
	>>> add1sec(0, 1, 2)
	(0, 1, 3)
	>>> add1sec(3, 5, 9)
	(3, 5, 10)
	>>> add1sec(19, 45, 59)
	(19, 46, 0)
	>>> add1sec(12, 59, 59)
	(13, 0, 0)
	'''
	#Check if parameters are correct
	if (0<=h<24) and (0<=m<60) and (0<=s<60):
		
		# Total time in seconds.
		totalTime = (h*3600) + (m*60) + s +1
		
 
		newHour =  0 if totalTime // 3600 == 24 else totalTime // 3600
		
		newMin = totalTime % 3600 // 60
		
		newSec = totalTime % 3600 % 60
		
		return newHour, newMin, newSec
	
	
	

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)


print(str.join( "aa", "bb" ))

print(''.join( ("aa", "bb") ))













