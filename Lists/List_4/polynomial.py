import sys 

x = float(sys.stdin.readline())

coef = sys.stdin.readline()

# 1 2 3 4 5

#coef = (1,2,3,4,5)


result = 0 
to = 0

for c in coef:
    c = float(c)
    
    result += c*(x**to)
    to +=1
    
print("{:.4f}".format(result))

