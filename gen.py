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
        
        if ranked_solutions[0][0] > 9999:
            break
        
        best_solutions = ranked_solutions[:100]
        
        elements_0 = []
        elements_1 = []
        elements_2 = []
        for element in best_solutions:
            elements_0.append(element[1][0])
            elements_1.append(element[1][1])
            elements_2.append(element[1][2])
        
        new_generation = []
        for i in range(1000):
            e1 = random.choice(elements_0) * random.uniform(0.99, 1.01)
            e2 = random.choice(elements_1) * random.uniform(0.99, 1.01)
            e3 = random.choice(elements_2) * random.uniform(0.99, 1.01)
            
            new_generation.append((e1, e2, e3))
            
        solutions = new_generation
            
if __name__ == "__main__":
    main()

