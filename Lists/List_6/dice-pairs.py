from easyinput import read

c = [0,0,0,0,0,0,0,0,0,0,0,0,0]

n = read(int)

while n is not None:
    c[n] += 1
    n = read(int)

for i in range(2,13):
    if c[i] != 0:
        print(i, ": ", c[i], sep='')
