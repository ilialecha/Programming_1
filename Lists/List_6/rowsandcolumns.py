import sys


n, m = sys.stdin.readline().split()
n = int(n)
m = int(m)

matrix = []

for i in range(n):
    row = sys.stdin.readline().split()
    matrix.append(row)

empty = sys.stdin.readline()

query = sys.stdin.readline()


while query != '':
    
    if "row" in query:
        print(query.strip(),": ", ' '.join(matrix[int(query.split()[1])-1]),sep="")  
    
    elif "column" in query:
        num_col = int(query.split()[1])
        tmp_col = []
        
        for i in range(n):
            tmp_col.append(matrix[i][num_col-1])
        
        print(query.strip(), ': ', ' '.join(tmp_col), sep='')
    
    elif "element" in query:

        row, column = query.split()[1:]

        row = int(row)
        column = int(column)

        print(query.strip() , ": " , matrix[row-1][column-1],sep='')
    
    query = sys.stdin.readline()

