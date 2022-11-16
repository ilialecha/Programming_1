def sort_no_dup(ns):
    '''
    >>> sort_no_dup([5, 1, 5, 2, 4, 1, 4, 8, 2, 1])
    [1, 2, 4, 5, 8]
    >>> sort_no_dup([])
    []
    >>> sort_no_dup([33, 33, 33, 33, 33, 33])
    [33]
    >>> sort_no_dup([7, 6, 7, 6, 7, 6])
    [6, 7]
    '''

    return list(set(ns))

    #ns.sort()
    #    for n in ns:
    #        while ns.count(n) > 1:
    #            ns.remove(n)
    #    return ns



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
