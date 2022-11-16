def many_few(f):
    v = []
    c = []
    vc = 0
    cc = 0
    for w in f:
        for l in w:
            if l in "aeiou": vc+=1
            else: cc+=1
        if cc > vc: c.append(w)
        else: v.append(w)
        vc,cc=0,0
    return c,v