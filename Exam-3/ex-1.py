from easyinput import read

n = read(int)
d = {}
for i in range(n):
    num = read(int)
    if num in d: d[num] += 1
    else: d[num] = 1

for k,v in sorted(d.items()): print(f"{k} : {v}")