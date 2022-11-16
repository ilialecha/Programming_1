def is_power7(n):
    p=0
    if n == 0:
        return False
    while n != 1:
        if n%7 != 0:
            return False
        n = n//7
        p+=1
    return True

def short_power7_chains(f,k):
    c=0
    for n in f:
        if is_power7(n) and c<k: c+=1
        elif not is_power7(n): c = 0
        else:
            return False
    return True
