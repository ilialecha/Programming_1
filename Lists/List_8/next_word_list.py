def next_word_list(s,l):
    f=None
    r=[]
    if not s in l or len(l)==0: return []
    for w in l:
        if w == s and f!=s: f=w
        elif f==s: r.append(w)
        f=w
    return r
