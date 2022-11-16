import sys

seq = sys.stdin.readline().strip().split()

res = []
'''
lens = tuple( len(i) for i in seq )
search = 0 
for len_ in lens:
    if lens.count(len_) >= 2:
        search = len_
        break
for word in seq:
    if len(res)==2:
        break
    if len(word)==search:
        res.append(word)
print(" ".join(res))
'''

index0 = 0
index1 = 0
last_diff = 0
lens = tuple( len(i) for i in seq )

print(lens)

for word in seq:
    for word_ in seq:
        if (index0 != index1) and ( len(word) == len(word_)): # Check that are not the same position in seq and len() to be equal
            last_diff = index0 - index1
            res.append(word+" "+word_)
            break
        index1 += 1
    index0 += 1
    index1 = 0

if not res:
    print("All words have different lengths")
else:
    print(res)   
