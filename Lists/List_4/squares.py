import sys

line = sys.stdin.readline()
while line!='':
    n = int(line)
    for i in range(0,n):
        print(str(n)*n)

    line = sys.stdin.readline()
    if line!='':
        print()

        