def leap_year(year):

    """A leap year (in the Gregorian calendar) occurs:

    In every year that is evenly divisible by 4.
    Unless the year is evenly divisible by 100, in which case it's only a leap         year if the year is also evenly divisible by 400.

    Parameter: year.
    Return: bool. """ 
    
    bool_year = False

    if year % 4 == 0 and year % 100 != 0:
        bool_year = True
    
    if year % 100 == 0 and year % 400 == 0:
        bool_year = True
            
    return bool_year
