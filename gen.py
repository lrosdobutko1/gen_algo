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
        
    for i in range(10000):
        ranked_solutions = []
        for s in solutions:
            ranked_solutions.append(
                (
                    fitness(
                        s[0], 
                        s[1],
                        s[2],
                        ),
                    s
                    )
                )
            
            ranked_solutions.sort(reverse=True)
            
        print(f"=== Best solutions in generation {i} ===")
        print(ranked_solutions[0])

if __name__ == "__main__":
    main()