from easyinput import read
from sys import stdin

p = read(int)
outcomes = dict()
for i in range(p):
    tmp = stdin.readline().split()
    if len(tmp) == 2:
        outcomes[tmp[0]] = float(tmp[1])
prized = 0
for i in sorted(outcomes, key=outcomes.get, reverse=True):
    if prized == 0:
        print("Gold:", i)
        prized += 1
    elif prized == 1:
        print("Silver:", i)
        prized += 1
    elif prized == 2:
        print("Bronze:", i)
        prized += 1
    else:
        print(i)