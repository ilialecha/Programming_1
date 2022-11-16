from sys import stdin

#number of lines containing word
nl = 0

#target word
tw = stdin.readline().strip()

#current line
cl = stdin.readline()


#check for the first instance of the target word in
#inputted line until there are no further lines
while cl != '':
	
	cl = cl.strip().split()
	found = False
	i = 0
	while not found and i < len(cl):
		if cl[i] == tw:
			found = True
			nl += 1
		else:
			i += 1
	
	cl = stdin.readline()

print(nl)
