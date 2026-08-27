"""Calculate the number of grains of wheat on a chessboard.

A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time."""

#The number of grains on a given square
def square(number):
    
    """When the square value is not in the acceptable range""" 
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
        
    #to iterate   
    iteration_square = 1 
    grains = 1
    
    while iteration_square != number:
        iteration_square = iteration_square + 1
        grains = grains * 2
    
    return grains

"""The total number of grains on the chessboard is calculated in the function below"""
def total():

    #to iterate
    iteration_total = 0 
    grains = 1
    total_grains = 0
    
    while iteration_total < 64:
        iteration_total = iteration_total + 1
        total_grains = total_grains + grains
        grains = grains * 2
        
    return total_grains
