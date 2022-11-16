
number = int(input())
results = (str(number)+"*"+str(i)+" = "+str(number*i) for i in range(1,11))

print(results)

for i in  results: print(i)
