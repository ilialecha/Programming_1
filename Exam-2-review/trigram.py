import sys
def trigrams(string):
    '''
    >>> trigrams('hello')
    ['hel', 'ell', 'llo']
    >>> trigrams('crocodile')
    ['cro', 'roc', 'oco', 'cod', 'odi', 'dil', 'ile']
    >>> trigrams('hi')
    []
    '''
    return list( string[i:i+3] for i in range(0,len(string)) if len(string[i:i+3])==3 )


def common_trigram(list1, list2):
    for elem1 in list1:
        for elem2 in list2:
            if elem1 == elem2:
                return True
    return False

seq = sys.stdin.readline().strip().split()

for i in range(0,len(seq)-1):
    if common_trigram(trigrams(seq[i]), trigrams(seq[i+1])):
        print (seq[i],seq[i+1])