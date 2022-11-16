from easyinput import read_line

string = read_line()
d = {}
l = []
while string is not None:
    string = string.split()

    for i in range(1,len(string)):
        if not string[i-1]+" "+string[i] in d: d[string[i-1]+" "+string[i]] = 1
        else: d[string[i-1]+" "+string[i]]+=1
        l.append(string[i-1]+" "+string[i])
    string = read_line()

d2={}

for i in sorted(l): ## Ordena clave
    if i.split()[0] in d2: d2[i.split()[0]].append(i.split()[1])
    else: d2[i.split()[0]] = [i.split()[1]]

for k,v in d2.items():
    tmp =[]
    if len(d2[k])>=2:
        for i in d2[k]:
            d2[k] = list(set(d2[k]))
            tmp.append(i + " " + str(round(d2[k].count(i)/len(set(d2[k])),3)) )
        d2[k] = tmp


for k,v in sorted(d2.items()):
    if len(d2[k])<2:
        continue
    else:
        n =len(d2[k])
        d2[k] = set(d2[k])
        print(f"{k} {n} : {' '.join(d2[k])}")