def transpose(m):
    n = len(m)
    for i in range(n):
        for j in range(i+1, n):
            m[i][j],m[j][i] = m[j][i],m[i][j]


m = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

transpose(m)

print(m)
