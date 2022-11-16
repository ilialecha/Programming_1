m = [
    [0,0,0], #0
    [0,0,0], #1
    [0,0,0] #2
]

m2 = [
    [2,1,1], #0
    [0,0,1], #1
    [0,0,0] #2
]
for row in range(len(m)):
    num1 = m[row].count(1)
    num_elems = len(m[row])
    for col in range(num_elems):
        if row == col:
            m[row][col] = num1
        else:
            if m[row][col] == 1:
                m[row][col] = -1


for row in m:
    for col in row:
        print(str(col)+" ", end="")
    print()
print()