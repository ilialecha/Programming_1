def jumps(x, k):
    '''
    >>> jumps([2, 1, 3, 5, 7, 4, 9, 5, 2, 5, 8], 0)
    [2, 3, 4, 5]
    >>> jumps([2, 1, 3, 5, 7, 4, 9, 5, 2, 5, 8], 1)
    [1, 3, 4, 5]
    >>> jumps([2, 1, 3, 5, 7, 4, 9, 5, 2, 5, 8], 3)
    [5, 2, 8]
    >>> jumps([2, 1, 3, 5, 7, 4, 9, 5, 2, 5, 8], 20)
    []
    >>> jumps([2, 1, 3], 1) + jumps([2, 1, 3, 5, 7], 4) 
    [1, 3, 7]
    '''
    result = []

    index = k 

    while index < len(x):
		#Añadimos a result el elemento de X que esta en la posicion index 
        result.append(x[index])

		#Comprobamos si index + elemento de X que esta en la posicion index
		# es mayor o igual que el numero de elementos en X
        if index + x[index] >= len(x):
            break #En caso de entrar aquí el programa termina (Linear search)
        index += x[index]

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
