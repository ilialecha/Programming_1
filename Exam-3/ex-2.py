from easyinput import read, read_line

r = read(int)
c = read(int)
found = False

for i in range(r):
    lis = []
    ant = read(int)
    lis.append(str(ant))
    for j in range(1,c):
        num = read(int)
        if ant < num:
            ant = num
            lis.append(str(num))
        elif ant > num: lis.clear()
    if len(lis) == c:
        print(" ".join(lis))
        found = not found
        break
if not found: print("No increasing row found.")
