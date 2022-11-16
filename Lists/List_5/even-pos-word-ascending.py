import sys

seq = sys.stdin.readline()
even_positions = []
if seq is not None:
    words = seq.split()
    even_positions, = list(word for word in words[1::2])


print(even_positions)
print(sorted(even_positions))