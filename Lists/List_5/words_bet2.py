import sys 

line = sys.stdin.readline().split()
if (not "beginning" in line or not "end" in line) or (len(line) -1 - line[::-1].index("end"))< line.index("beginning"):
    print("wrong sequence")
else:
    print(len(line[line.index("beginning")+1:len(line) - 1 - line[::-1].index("end")]))