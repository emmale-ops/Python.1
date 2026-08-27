""" Write some code to determine whether a number is an Armstrong number"""

def is_armstrong_number(number):
    
    digits = str(number)
    power = len(digits)
    total = 0
    
    for digit in digits:
        total = int(digit)**power + total

    return total == number
