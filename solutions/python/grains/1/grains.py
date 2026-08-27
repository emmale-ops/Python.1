"""Calculate the number of grains of wheat on a chessboard.

A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time."""

"""The number of grains on a given square"""
def square(number):
    
    """When the square value is not in the acceptable range""" 
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
        
    #to iterate   
    i = 1 
    grains = 1
    
    while i != number:
        i = i + 1
        grains = grains * 2
    
    return grains

"""The total number of grains on the chessboard"""
def total():

    #to iterate
    i = 0 
    grains = 1
    total_grains = 0
    
    while i < 64:
        i = i + 1
        total_grains = total_grains + grains
        grains = grains * 2
        
    return total_grains
