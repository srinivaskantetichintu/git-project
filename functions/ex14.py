def addFirstAndLast(x): 
    if len(x) == 0:
        return 0
    elif len(x) == 1:
        return x[0]
    else:
        return x[0] + x[-1]
print(addFirstAndLast([1,2,3,4])