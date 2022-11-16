from sympy import *
from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False)

A=Matrix([[1,2,3],[3,0,4],[6,4,5]])

b=Matrix([[1,2,3]])


#iA = A.inv()*b

print(A)

print(b)

