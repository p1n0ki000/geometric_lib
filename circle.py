import math


def area(r):
    '''
    Calculates the area of a circle from the radius.

    argument:
        r (int): radius of a circle

    return value:
        (float): area of a circle

    example:
        >> area(2);
        12,56637061
'''
    
    return math.pi * r * r


def perimeter(r):
    '''
    Calculates the circumference of a circle from the radius.

    arguments:
        r (int): radius of a circle

    return value:
        (float): circumference of a circle

    example:
        >> perimetr(4);
        25,13274123
    '''
    return 2 * math.pi * r

