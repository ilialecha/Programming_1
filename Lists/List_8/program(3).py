from easyinput import read

f, s = read(int), read(int)
found, ff = False, False

n = read(int)
d = []

while n is not None and not found:
	if n == f and not ff:
		ff = True
	elif ff and n != s:
		d.append(n)
	elif ff and n == s:
		found = True
	
	n = read(int)

if not found:
	print('nonexistent section')
elif found and d == []:
	print('empty section')
else:
	print(f'maximum is: {max(d)}')
		
