import sys 

seq = sys.stdin.readline()

res = -1

while seq != "":

    if sum(1 for i in seq.strip("\n").split() if int(i)%10==3) % 2 ==0:
        res = sum(int(i) for i in seq.strip("\n").split())
        break
    
    seq = sys.stdin.readline()

print(res)