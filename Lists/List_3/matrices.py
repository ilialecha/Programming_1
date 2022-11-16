from sympy import *

from sympy.interactive.printing import init_printing

init_printing(use_unicode=False, wrap_line=False)

#Crear matriz 

D = Matrix( [ [0,0,0.33] , [0.18,0,0] , [0, 0.71, 0.94] ] )
'''
A)
1. children born 
2.Number of 2020 is 18% that children survived
3.

B)

C)
K+1 = m*V+1
Vk+10 = Matrix * 10  
'''
E = Matrix( [ [33,36,165] ] ) 
E_D = E*D


#Exercise 2

A_2=Matrix([[1,8,6],[3,5,7],[4,9,2]])
B_2=Matrix([[6,8,7,3],[3,5,4,1]])
C_2=Matrix([[1,2],[1,2]])

b_2 = Matrix([[1],[-2],[1]])
c_2 = Matrix([[1],[8]])
d_2 = Matrix([[1],[-1],[0],[1]])
e_2 = Matrix( [[1],[1]] )


#2-A and 2-B:

#print( A_2.rref() )

#print(A_2.rank())

#print("\n")

#print( B_2.rref() )
#print(B_2.rank())
#print(B_2.T.rank())

#print("\n")

'''
print( C_2.rref() )
print(C_2.rank())

print("\n")

print( b_2.rref() )
print(b_2.rank())

print("\n")

print( c_2.rref() )
print(c_2.rank())

print("\n")

print( d_2.rref() )
print(d_2.rank())

print("\n")

print( e_2.rref() )
print(e_2.rank())
'''


#Ejercicio 3 A

A_3=Matrix([[1,2,3],[4,5,6],[7,8,9]])


#print(A_3.rref())


# u1 = (1, 1, 1), u2 = (1, 2, 3) and u3 = (2, −1, 1). en una matrix 



#e1 space vectors
A_1 = Matrix([[1,1,2],[1,2,-1],[1,3,1]])


v = Matrix([[1],[-2],[5]])

#print (A_1*v)


c6 = Matrix( [ [1,-2,5,3],[2,3,1,-4],[3,8,-3,-5] ] )

print(c6.rref())















