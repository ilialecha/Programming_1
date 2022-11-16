def count_them(l,k):
    r=[]
    for i in range(len(l)):
        if str(k) in str(l[i]): r.append(i)
    return r