from easyinput import read
n,k,seq = read(int),read(int),read(int)
nums = {}
found = False

while seq is not None and not found:
    if seq % n == 0:
        if seq in nums and nums[seq] + 1 < k: nums[seq] += 1
        elif seq in nums and nums[seq]+1 == k:
            print(seq)
            found = not found
        else: nums[seq] = 1
    seq=read(int)

if not found: print("none")