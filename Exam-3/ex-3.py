from easyinput import read

def squarematrix(rowcol):
    # Creating square matrix given rowcol parameter.
    matrix = []
    for row in range(rowcol):
        tmp = []
        for i in range(rowcol):
            tmp.append(read())
        matrix.append(tmp)
    return matrix

def process(matrix):
    for row in range(len(matrix)):
        ones = " ".join(matrix[row]).count("1")
        for col in range(len(matrix[row])):
            if matrix[row]== matrix[col]: matrix[row][col] = str(ones)
            else: matrix[row][col] = str(-1 * int(matrix[row][col]))
    return matrix

n=read(int)
mat = squarematrix(n)
res = process(mat)
for e in res : print(" ".join(e)+" ", end="\n")
print()