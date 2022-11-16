from easyinput import read_line

seq = read_line()

lines = []

while seq is not None:
    line = seq
    lines.append(line.split())
    seq = read_line()

for line in lines[1:]:
    count = 0
    for i in range(0,len(line)-1):
        if int(line[i]) < int(line[i+1]):
            count += 1
    print(count)
        