from easyinput import read_many

s = [num for num in read_many(int)]

s.reverse()
c = 0
for i in s[1:-1]:
    if i == s[0]:
        c +=1

print(c)