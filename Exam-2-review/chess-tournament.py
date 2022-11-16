from easyinput import read_line

seq = read_line()
seqs = []
while seq is not None:
    seqs.append(seq.split())
    seq = read_line()

print(seqs)


'''
5
Marta Juan Pedro Ana Javier
Marta Pedro 1-0
Ana Juan 1/2-1/2
Pedro Juan 0-1

2 alice bob alice bob 1/2-1/2 
bob alice 0-1 alice bob 0-1 


'''