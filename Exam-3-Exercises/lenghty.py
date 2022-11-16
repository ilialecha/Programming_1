from easyinput import read

word = read()
words = dict()
found = False
#Proceso lectura de palabras----------------
while word is not None:
    # Hacer lo que sea
    if not len(word) in words:
        words[len(word)] = [word]
    else:
        words[len(word)].append(word)
    word = read()
#--------------------------------------------
#Buscando resultado
for element in sorted(words, reverse=True):
    if len(words[element]) > 1:
        print(' '.join(words[element]))
        found = not found
        break

if not found: print("All words have different lengths")
