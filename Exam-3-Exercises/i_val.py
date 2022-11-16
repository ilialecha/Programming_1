def i_val(lst):
    '''
    >>> i_val(['Dec16of2019', 'a1B2c3D'])
    [123, 162019]
    >>> i_val(['a21', 'b2']) + i_val(['1j5k'])
    [2, 21, 15]
    >>> i_val(['456x654', 'NoDigitsHere', 'xyz7zxy', '007Bond', ''])
    [0, 0, 7, 7, 456654]
    >>> i_val([])
    []
    '''
    result = []
    for elem in lst:
        tmp = []
        if len(elem):
            for num in elem:
                if num.isdigit(): tmp.append(num)
            if not len(tmp): tmp.append('0')
        else:
            tmp.append('0')
        result.append(int(''.join(tmp)))
    return sorted(result)


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

