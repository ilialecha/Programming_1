from easyinput import read

n,k,x = read(int)
nf = True
d = dict()
while x is not None:
    if x % n == 0:
        if x in d and d[x]+1==k: print(f"")
    x = read(int)