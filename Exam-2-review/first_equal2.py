from easyinput import read_line

seq = read_line()
seen = []
match = False
for word in seq.split():
    if len(word) in seen:
        print(seq.split()[seen.index(len(word))], word)
        match = True
        break
    else:
        seen.append(len(word))
if not match:
    print("All words have different lengths")