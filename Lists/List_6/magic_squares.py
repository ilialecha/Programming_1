from easyinput import read


def squarematrix(rowcol):
    # Creating square matrix given rowcol parameter.
    matrix = []
    for row in range(rowcol):
        tmp = []
        for i in range(rowcol):
            tmp.append(read(int))
        matrix.append(tmp)
    return matrix


def check_values(matrix):
    n = len(matrix)
    seen = [0] * (n * n + 1)
    # seen = [0 for i in range(n*n+2)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 1 or matrix[i][j] > n * n:
                return False
            elif seen[matrix[i][j]]:
                return False
            else:
                seen[matrix[i][j]] = True
    return True


def is_magic(matrix):
    prev = sum(matrix[0])
    d_p = 0
    d_i = 0

    if not check_values(matrix):
        return "no"

    # Checking diagonals:
    for i in range(len(matrix)):
        d_p += matrix[i][i]
        d_i += matrix[i][len(matrix) - 1 - i]
    if d_p != prev or d_i != prev:
        return "no"

    # Checking rows & col
    for i in range(1, len(matrix)):
        if sum(matrix[i]) != prev:
            return "no"
        if sum_colum(matrix, i) != prev:
            return "no"

    return "yes"


def sum_colum(matrix, j):
    sc = 0
    for i in range(len(matrix)):
        sc += matrix[i][j]
    return sc


print(None == True)
rowcol = read(int)

while rowcol is not None:
    matrix = squarematrix(rowcol)

    print(is_magic(matrix))

    rowcol = read(int)

# Check if transposing matrix is accepted by jutge.
