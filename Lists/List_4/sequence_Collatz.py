import sys

line = sys.stdin.readline() #Obtain Data
while line!='':
    n = int(line)
    steps = 0 
    while n != 1:
        if n%2==0:
            n //= 2
        else:
            n *= 3
            n += 1
        steps+=1

    print(steps)
    line = sys.stdin.readline()

