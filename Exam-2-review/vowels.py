import easyinput

seq = easyinput.read()
even = 0
v = ['a', 'e', 'i', 'o', 'u']

while seq != None: #Mientras la linea no sea ""

	#Quitamos espacios al principio y final. Y dividimos elementos por espacios.
	seq = seq.strip().split()	# Ejemplo: hola que tal --> ["hola","que","tal"]

	for word in seq: #Recorremos cada palabra
		vowels = 0
		
		for letter in word: # Recorremos cada letra de cada palabra
			if letter.lower() in v:
				vowels += 1
		#Una vez a recorrido todas las letras de una palabra
		#comprueba si el numero de vocales es par o impar 
		if vowels % 2 == 0 or vowels == 0:
			even += 1
	#Leemos otra linea 
	seq = easyinput.read()

print(even)
