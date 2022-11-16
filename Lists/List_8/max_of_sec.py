from easyinput import read,read_many,read_line

a,b,c = read(int),read(int),read(int)
while a is not None:
    a_s=False
    b_s=False
    l=[]
    for i in range(c):
        n = read(int)
        if n==a and not a_s:
            a_s=True
            continue
        if n==b: b_s = True
        if a_s and not b_s: l.append(str(n))
    if not b_s: l.clear()
    if len(l) == 0: print("----------")
    print(" ".join(l)+" ")
    a, b, c = read(int), read(int), read(int)


