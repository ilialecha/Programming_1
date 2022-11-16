from easyinput import read

a,w,d,nf = read(int), read(), dict(), True

while w is not None:
    if w in d:
        if d[w]+1 > a:
            print(f'The first word to reach above frequency {a} is "{w}".')
            nf = not nf
            break
        else: d[w] += 1
    else: d[w] = 1
    w = read()

if nf: print(f"No words reach above frequency {a}.")