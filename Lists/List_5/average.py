from easyinput import read_line

seq = read_line()


print( "%.2f" % (( sum( float(i) for i in seq.split() ) )/len(seq.split())) )