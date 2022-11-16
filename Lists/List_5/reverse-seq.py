from easyinput import read_line

seq = read_line()
results = []

while seq is not None:
    results.append( list( i for i in ( seq.split()[1:] )[-1::-1] ) )
    seq = read_line()

for result in results: print(" ".join(result))