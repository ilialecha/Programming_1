import sys

alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

code = sys.stdin.readline()

lines = int(sys.stdin.readline())

while code != "":

    for i in range(lines):
        text = sys.stdin.readline().strip()
        
        #translate
        for char in text:
            if char == "_":
                letter = " "
            else:
                pos = code.index(char)
                letter = alf[pos]
            print(letter, end="")

        print()

    print()
    empty = sys.stdin.readline()
    code = sys.stdin.readline()
