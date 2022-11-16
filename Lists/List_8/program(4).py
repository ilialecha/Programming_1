from easyinput import read

f, s, sz = read(int), read(int), read(int)

while f:
	found = False
	a = False
	b = False
	d = []

	for _ in range(sz):
		cv = read(int)
		
		if not a and not b and cv == f:
			a = True
			
		elif a and not b and cv != s:
			d.append(cv)

		elif a and not b and cv == s:
			found = True
			b = True

	if found:
		for n in d:
			print(f'{n} ', end = '')
		print()
	else:
		print()

	print('----------')
	
	f, s, sz = read(int), read(int), read(int)
