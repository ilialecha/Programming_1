from easyinput import read
n = read(int)
m = read(int)
w = read()
res = []
found = False
while w is not None:
    if len(w) >= m:
        res.append(w) ; if len(set(res))==n: found = not found ; print("\n".join(sorted(set(res))))
    if found: break
    w = read()

if not found: print("Goal not attained")