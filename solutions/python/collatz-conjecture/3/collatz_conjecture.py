"""Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture"""

def steps(number):
    step = 0
    
    """If the integer is equal o below zero, return an error"""
    if  number <= 0:
        raise ValueError("Only positive integers are allowed")
        
    while number > 1:
        step = step + 1
        if number%2 == 0:
            number = number//2
        else:
            number = number*3 + 1
    return step
