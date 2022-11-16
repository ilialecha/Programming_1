from easyinput import read

word = read()
words = dict()
showed = False
while word is not None:
    if not len(word) in words:
        words[len(word)] = [word]
    else:
        words[len(word)].append(word)
    word = read()

for group in sorted(words, reverse=True):
    if len(words[group]) > 1:
        print(' '.join(words[group]) )
        showed = not showed

        break

if not showed: print("All words have different lengths")
