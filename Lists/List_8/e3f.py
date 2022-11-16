from easyinput import read_many, read, read_line
def second_largest_values(m):
    r = []
    for l in m:
        r.append(sorted(l)[1])
    return r

l = read_line()
m=[]
while l is not None:
    m.append(l.split())
    l = read_line()
for r in range(len(m)):
    print(f"second largest in row {r} is {sorted(set(m[r]), key=int, reverse=True)[1]}")
