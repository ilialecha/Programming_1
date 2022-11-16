def max_overlap(s,t):
    '''
    >>> max_overlap('bugs', 'bunny')
    'bu'
    >>> max_overlap('winter', 'winner')
    'win'
    >>> max_overlap('hand', 'made')
    ''
    >>> max_overlap('x', 'x')
    'x'
    '''
    iterations = len(s) if len(s) <= len(t) else len(t)
    
    overlap_in = 0
    
    if s == t: 
        return s
    if iterations and s[0] != t[0]: 
        return ""

    for i in range(iterations):
        if s[0:i] == t[0:i]: 
            overlap_in = i
        else: 
            return s[0:overlap_in]
    

# This will run the function on the test examples
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)