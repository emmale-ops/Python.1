"""Calculate the points scored in a single toss of a Darts game"""

def score(x, y):
    
    """If the dart lands outside the target, player earns no points (0 points).
    If the dart lands in the outer circle of the target, player earns 1 point.
    If the dart lands in the middle circle of the target, player earns 5 points.
    If the dart lands in the inner circle of the target, player earns 10 points."""
    
    coo = x**2 + y**2
    
    if coo <= 1:
        return 10
        
    if coo <= 25:
        return 5
    
    if coo <= 100:
        return 1

    return 0