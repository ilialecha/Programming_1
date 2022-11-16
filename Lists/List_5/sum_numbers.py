import easyinput
num = easyinput.read(int)
res = []

while num is not None:
    res.append("The sum of the digits of "+str(num)+" is "+str(sum((int(n) for n in str(num))))+".")
    num = easyinput.read(int)

for i in res: print(i)