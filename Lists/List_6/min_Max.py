def min_Max(matrix):
    '''
    >>> min_Max([[1,2,3],[3,1,2],[2,3,1]])
    [[1, 3], [1, 3], [1, 3]]
    >>> min_Max([[100]])
    [[100, 100]]
    >>> min_Max([[2,2],[2,2]])
    [[2, 2], [2, 2]]
    >>> min_Max([[17, 4],[1,1]])
    [[4, 17], [1, 1]]
    >>> min_Max([[5, 1, 2, 1, -2],[1,21,-1,-2,8],[2,3,1,6,6],[1,2,3,4,5]])
    [[-2, 5], [-2, 21], [1, 6], [1, 5]]
    '''
    return [[min(matrix[row]), max(matrix[row])] for row in range(len(matrix))]
    
# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)

