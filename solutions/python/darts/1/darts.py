def score(x, y):

    coo = x**2 + y**2
    
    if coo <= 1:
        return 10
    elif coo <= 25:
        return 5
    elif coo <= 100:
        return 1
    else:
        return 0


