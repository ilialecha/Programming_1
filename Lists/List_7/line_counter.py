from easyinput import read,read_line

target = read()

text = read_line()
count = 0
line_found = False
while text is not None:
    if target in set(text.split()): count +=1
    text = read_line()
print(count)