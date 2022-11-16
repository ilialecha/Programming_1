def sum_of_digits_sorted(f):
    '''
    >>> sum_of_digits_sorted([56, 2131])
    [2131, 56]
    >>> sum_of_digits_sorted([313, 44, 36, 11111, 35, 26, 7])
    [11111, 7, 313, 26, 35, 44, 36]
    >>> sum_of_digits_sorted([9, 53, 511, 4000, 10001, 45])
    [10001, 4000, 511, 53, 9, 45]
    '''
    res = {}

    for num in f:
        res[num] = sum(int(i) for i in str(num))
    
    return [k for k, v in sorted(res.items(), key=lambda item: item[1])]


# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)