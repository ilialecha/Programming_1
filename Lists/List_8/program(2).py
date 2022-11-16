from easyinput import read

out = {}

case = read(int)
while case is not None:
	for _ in range(2):
		for _ in range(case):
			ij = (read(int), read(int))
			v = read(int)
			#print(ij, v)
			if ij not in out:
				out[ij] = v
			else:
				out[ij] += v
			#print(out)
		case = read(int)
	
	m = []
	for key in out:
		if out[key] != 0:
			m.append([key[0], key[1], out[key]])
	
	if m != []:
		for n in sorted(m):
			print(f'{n[0]} {n[1]} {n[2]}')
		print('----------')
	else:
		print('----------')
	
	out = {}
