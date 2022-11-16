import sys 

line = sys.stdin.readline().split()

c = 0

do_count = False
b_seen = False
e_seen = 0
total_end = line.count("end")
if ("beginning" not in line) or ("end" not in line):
    print("wrong sequence")

elif line.index("end") < line.index("beginning") and line[-1] != "end":
    print("wrong sequence")

else:
    for word in line:
        if word == "beginning" and not b_seen:
            do_count, b_seen = True, True
            continue
        elif word == "end" and e_seen < total_end:
            e_seen +=1
        elif word == "end" and e_seen:
            break
        elif do_count and  e_seen!=total_end:
            c += 1
        print(word,c)
    c += line.count("end")-1
    print(c, end="\n")