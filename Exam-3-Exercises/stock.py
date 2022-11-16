def total_stock(stk1,stk2):
    for k,v in stk1.items():
        if k in stk2: stk2[k] += v
        else: stk2[k] = v
    return stk2
