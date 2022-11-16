from easyinput import read

a,b,n = read(int), read(int),read(int)

fa, fb = False, False
finish = False
l=[]
while n is not None and not finish:
    if not fa and not fb and n==a:
        fa = not fa
    elif fa and not fb and n != b:
        l.append(n)
    elif fa and not fb and n ==b:
        finish = not finish
        fb = not fb
    n = read(int)
if finish and len(l)>0: print(f"maximum is: {sorted(l)[-1]}")
elif finish and len(l)==0: print("empty section")
else: print("nonexistent section")