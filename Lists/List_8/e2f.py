from easyinput import read_line
o = {}
l = read_line()
f = False
n = 1
if l is not None: o[0] = l.split()
l=read_line()
while l is not None and not f:
    for w in l.split():
        if w in o[n-1] and not f:
            print(f"Found: {w}")
            f = not f
        else: o[n] = l.split()
    l = read_line(); n+=1

if not f: print("Found nothing")