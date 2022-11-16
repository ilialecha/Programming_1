import sys

seq = sys.stdin.readline()
seqs = []
res = []
while seq != "":
    seqs.append(seq.strip("\n"))
    seq = sys.stdin.readline()

for seq in seqs:
    for num in seq.split():
       if int(num) % 7 == 0:
           res.append(int(num))

res.sort()
if len(res) == 0:
    output= "No multiples of 7"
else:
    output = "Multiples of 7: "
for i in res:
    output += str(i)+" "

print(output.rstrip(" "))