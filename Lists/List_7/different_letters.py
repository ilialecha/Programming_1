def num_dif_letters_list(l):
    '''
    >>> num_dif_letters_list(['alea', 'iacta', 'est'])
    [3, 4, 3]
    >>> num_dif_letters_list(['', 'z', 'zz', 'zzz', 'zzzz'])
    [0, 1, 1, 1, 1]
    >>> num_dif_letters_list([])
    []
    >>> num_dif_letters_list(['atalaya', 'orinoco', 'pasas', 'elixir'])
    [4, 5, 3, 5]
    '''
    return [len(set(w)) for w in l]

