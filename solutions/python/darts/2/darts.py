"""Calculate the points scored in a single toss of a Darts game"""
def score(x, y):

    coo = x**2 + y**2
    
    if coo <= 1:
        return 10
        
    if coo <= 25:
        return 5
    
    if coo <= 100:
        return 1
    else:
        return 0