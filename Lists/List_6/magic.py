import sys
import sympy as np

seq = sys.stdin.readline()
seqs = []
while seq != "":
    seqs.append(seq.rstrip("\n").split())
    seq = sys.stdin.readline()

for s in range(0,len(seqs)):
    if len(seqs[s]) == 1:
        square = [seqs[s+1:s+1+int(seqs[s][0])]]
        ant = None
        for row in square[0]:
            if ant is None:
                
                ant = sum(int(i) for i in row)
            
            elif ant != sum(int(i) for i in row):
