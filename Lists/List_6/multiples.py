from easyinput import read

ant = read(int)
num = read(int)
res = 0

while num is not None:
    if (ant==num==0) or (ant != 0 and num % ant == 0) : res += 1
    ant = num
    num=read(int)
print(res)