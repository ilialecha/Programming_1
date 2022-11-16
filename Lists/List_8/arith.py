from easyinput import read
n,r,s =read(int),read(int),read(int)
l=[]
ant = None
found = False
added = False


while s is not None and not found:
    if ant is None: ant = s
    elif ant+r == s:
        if not added: l.append(str(ant)); added = True
        l.append(str(s))
        ant = s
        if len(l)==n:
            found= not found
            print(" ".join(l))
    else:
        ant = s
        l.clear()
    s = read(int)

if not found: print(f"No arithmetic progression found with step {r} and length at least {n}")