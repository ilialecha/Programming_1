import sys

def productdigits(n):
    prod = 1
    for d in n:
        prod += int(d)

num = sys.stdin.readline().strip("\n")

while len(num)>1:
    x = productdigits(num)
    print(n,x)
    num = x


