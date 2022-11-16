from easyinput import read
w = read()
ws = dict()
while w is not None:
    if len(w)>2:
        if w[-3:] in ws:
            ws[w[-3:]].append(w)
        else:
            ws[w[-3:]] = [w]
    w = read()
for k,v in sorted(ws.items()):
    if len(set(v)) > 1 :
        print(f"{k}: {len(set(v))} {' '.join(sorted(set(v)))}")