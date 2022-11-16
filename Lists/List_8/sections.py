from easyinput import read

a ,b, c = read(int), read(int),read(int)

while a:

    fa, fb = False, False
    finish = False
    l=[]
    for i in range(c):
        n=read(int)
        if not fa and not fb and n==a:
            fa = not fa
        elif fa and not fb and n != b:
            l.append(n)
        elif fa and not fb and n ==b:
            finish = not finish
            fb = not fb

    if finish:
        for n in l: print(n,end=" ")
        print()
    else:
        print()
    print('----------')
    a, b, c = read(int), read(int), read(int)