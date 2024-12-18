import random

def equation(a, b, c):
    return 23*a**4 + 4*b**2 * 11*c**3 - 100

def fitness(a, b, c):
    ans = equation(a, b, c)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)
    
def main():
    solutions = []
    for s in range(1000):
        solutions.append( 
            (
                random.uniform(0,1000), 
                random.uniform(0,1000),
                random.uniform(0,1000), 
                )
            )
        
    print(solutions[:5])

if __name__ == "__main__":
    main()