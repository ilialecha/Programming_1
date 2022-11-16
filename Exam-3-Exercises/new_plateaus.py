#Gracias Diego :)
from easyinput import read

n = read(int)
found = False
num = read(int)
l = []
while num is not None and not found:
    l.append(num)
    if len(l) > n : l.pop(0)
    num = read(int)
    if len(l) == n and len(set(l)) == 1: found = not found

if found: print(f"A plateau of {l[0]}'s of length at least {n} occurs.")
else: print(f"No plateau of length {n} occurs.")