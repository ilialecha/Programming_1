from easyinput import read

line = read()
letters = dict()
while line is not None:
    for letter in line:
        if letter.islower():
            if letter in letters: letters[letter] +=1
            else: letters[letter] = 1
    line = read()


max = None
tmp_list = []
for v in sorted(letters, key=letters.get, reverse=True):
    if not max: max = letters[v] ; tmp_list.append(v+" "+str(letters[v]))
    elif max == letters[v] and tmp_list[0].split()[0] > v:
        tmp_list.pop(0) ; tmp_list.append(v+" "+str(letters[v]))

print(tmp_list[0])