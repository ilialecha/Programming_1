from easyinput import read
n = read(str)
l = []
while n != "END":
    l.append(n)
    n = read(str)

for i in sorted(l):
    print(i)