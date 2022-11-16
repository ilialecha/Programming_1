import sys

seq = sys.stdin.readline()

last_a = sum((1 for i in seq.split() if i[0] == 'a'))
result = "Not found"

while seq !="":

    a = sum((1 for i in seq.split() if i[0].lower() == i[0] and i[0] == 'a'))

    if a > last_a:
        result = seq
        break


    seq = sys.stdin.readline()
    """
    When in Rome, do as the Romans
A picture is worth a thousand words
There's no such thing as a free lunch
a penny saved is a penny earned
alfa beta
beta Alfa alfa
omega 
    """

print(result)
