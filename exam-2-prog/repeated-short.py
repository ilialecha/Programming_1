import sys
def repeated_short(lw):
    '''
    >>> repeated_short(['easy','come','easy','go','will','you','let','me','go'])
    ['easy', 'go']
    >>> repeated_short(['I','can','see','it','can','you','see','it'])
    ['can', 'it', 'see']
    >>> repeated_short(['unbelievable','unbelievable'])
    []
    '''
    
    l2 = list(set((word for word in lw if len(word)<5 and lw.count(word)>1)))
    l2.sort()
    return l2



seq = sys.stdin.readline()

i=1

while seq != "":
    if len(seq.strip("\n").split()) <=1:
        print(0,"")
    else:
        data = repeated_short(seq.split())
        result = " ".join(data) if len(data)>1 else "".join(data)
        print(len(repeated_short(seq.split())), result)
        i+=1
    seq = sys.stdin.readline()
