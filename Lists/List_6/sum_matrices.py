def sum(a,b):
    loops = len(a)
    for row in range(loops):
        for col in range(loops):
            a[row][col] += b[row][col]
    return a

def squarematrix(rowcol):
    # Creating square matrix given rowcol parameter.
    matrix = []
    for row in range(rowcol):
        tmp = []
        for i in range(rowcol):
            tmp.append(read(int))
        matrix.append(tmp)
    return matrix
