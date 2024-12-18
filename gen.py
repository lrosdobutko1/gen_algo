import random

def equation(a, b, c):
    return 23*a**4 + 4*b**2 * 11*c**3 - 100

def fitness(a, b, c):
    ans = equation(a, b, c)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)
    