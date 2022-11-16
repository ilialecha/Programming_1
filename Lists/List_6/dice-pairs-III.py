import sys

c = [0,0,0,0,0,0,0,0,0,0,0,0,0]

n = sys.stdin.readline()

first = True

while n != "":  

    if not first:
        print('-----')
    else:
        first = False

    c = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    #nint = [int(i) for i in n.split()]

    for n in n.split():
        c[int(n)] +=1
    
    for i in range(2,13):
        if c[i] != 0:
            print(i, ": ", c[i], sep='')


    n = sys.stdin.readline()

    
