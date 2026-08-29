def equilateral(sides):
    
    a, b, c = sides
    bool_equilateral = False
    sum1 = a + b
    sum2 = b + c
    sum3 = a + c

    if a > 0 and b > 0 and c > 0:
        if sum1 > c and sum2 > a and sum3 > b:
            if a == b == c:
                bool_equilateral = True

    return bool_equilateral


def isosceles(sides):

    a, b, c = sides
    bool_isosceles = False
    sum1 = a + b
    sum2 = b + c
    sum3 = a + c

    if a > 0 and b > 0 and c > 0:
        if sum1 > c and sum2 > a and sum3 > b:
            if a == b or b == c or a == c:
                bool_isosceles = True

    return bool_isosceles
                

def scalene(sides):

    a, b, c = sides
    bool_scalene = False
    sum1 = a + b
    sum2 = b + c
    sum3 = a + c

    if a > 0 and b > 0 and c > 0:
        if sum1 > c and sum2 > a and sum3 > b:
            if a!=b and b!=c and a!=c:
                bool_scalene = True
                
    return bool_scalene

