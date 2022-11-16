from easyinput import read, read_line

players = dict()
pos = 1

for i in range(read(int)):
    line = read_line().split()
    players[int(line[1])] = line[0]


for elem in sorted(players, reverse=True):
    if pos == 1: print("Gold: ", players[elem])
    elif pos == 2: print("Silver: ", players[elem])
    elif pos == 3: print("Bronze: ", players[elem])
    else: print(players[elem])
    pos +=1

