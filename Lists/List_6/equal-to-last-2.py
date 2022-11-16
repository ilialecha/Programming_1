from easyinput import read_many
import sys


# Efficient way 
s = [num for num in read_many(int)]
s.reverse()
c = 0
result =  sum([1 for i in s[1:] if i == s[0]] )
print(result)

#Other way 
s = [num for num in read_many(int)]

s.reverse()
c = 0
for i in s[1:]:
    if i == s[0]:
        c +=1

print(c)


# Inefficient way
n = sys.stdin.readline()

line = sys.stdin.readline().split()

last = len(line)-1
c = 0 
for i in range(0, len(line)-1):
    if line[i] == line[last]:
        c+=1

print(c)