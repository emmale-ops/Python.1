def leap_year(year):

    bool_year = False
    
    if year % 4 == 0 and year % 100 != 0:
        bool_year = True
    
    if year % 100 == 0 and year % 400 == 0:
        bool_year = True
            
    return bool_year
