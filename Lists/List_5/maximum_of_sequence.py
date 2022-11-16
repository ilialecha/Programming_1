import easyinput

seq = easyinput.read_line()
seqs = []
i = 0
while seq is not None :
    seq_ = list(int(n) for n in seq.split()[1:])
    seq_.sort(reverse=True)
    seqs.append(seq_[0])
    seq = easyinput.read_line()

for seq in seqs:
    print(seq)