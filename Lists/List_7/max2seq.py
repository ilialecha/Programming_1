def max2freq(l):
    '''
    >>> print(max2freq([ 40, 30, 40, 32, 41, 10, 41, 31, 31,40, 41, 40, 41, 30, 32, 32, 30, 31, 11 ]))
    ([40, 41], [30, 31, 32])
    >>> max2freq([ 20, 20, 10, 30, 30, 21, 21, 30 ])
    ([30], [20, 21])
    '''
    f = {}
    for e in l:
        if e in f: f[e] +=1
        else: f[e] = 1

    checked = 0
    l_index = None
    r0,r1=[],[]

    for k in sorted(f, key=f.get, reverse=True):
        if not l_index or l_index != f[k]: l_index = f[k] ; checked += 1
        if checked <= 2 and f[k] == l_index:
            if checked == 1: r0.append(k)
            else: r1.append(k)
    return sorted(r0), sorted(r1)

# This will run the function on the test examples
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
