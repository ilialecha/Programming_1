import sys
line = sys.stdin.readline() #Obtain Data

while line!='': #While obtained data different of " " will entry
    n = int(line)
    num = 0
    for i in range(0,n):
        for j in range(num, num+n):
            print(num%10, end="")
            num = num+1
        print()
    line = sys.stdin.readline()
    if line!='':
        print() 