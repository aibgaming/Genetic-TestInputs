# genetic_algorithm.py
import random

# Genetic Algorithm Parameters
POPULATION_SIZE = 50
GENERATIONS = 20
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2
ARRAY_SIZE = (2, 10)  # Minimum and maximum size of the input array
VALUE_RANGE = (-100, 100)  # Range of integers for array elements
TARGET_RANGE = (-200, 200)  # Range for target values

def fitness(test_input, target, target_function):
    """
    Fitness function based on code coverage and mutant detection.
    """
    # Run coverage analysis
    from coverage import Coverage
    cov = Coverage()
    cov.start()
    target_function(test_input, target)
    cov.stop()
    cov.save()
    coverage_percentage = cov.report(file=None, show_missing=False)
    
    # Simulate mutant detection (replace with MutPy later)
    mutants_killed = 0  # Mock value for demonstration
    return coverage_percentage + mutants_killed  # Weight coverage and mutants equally

def initialize_population():
    """
    Initialize the population with random test cases.
    """
    return [
        ([random.randint(*VALUE_RANGE) for _ in range(random.randint(*ARRAY_SIZE))], random.randint(*TARGET_RANGE))
        for _ in range(POPULATION_SIZE)
    ]

def crossover(parent1, parent2):
    """
    Perform crossover between two parents.
    """
    if random.random() > CROSSOVER_RATE:
        return parent1, parent2
    split = random.randint(1, len(parent1[0]) - 1)
    child1 = (parent1[0][:split] + parent2[0][split:], parent1[1])
    child2 = (parent2[0][:split] + parent1[0][split:], parent2[1])
    return child1, child2

def mutate(individual):
    """
    Perform mutation on an individual.
    """
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(individual[0]) - 1)
        individual[0][idx] = random.randint(*VALUE_RANGE)

def select(population, fitness_scores):
    """
    Select an individual using tournament selection.
    """
    tournament = random.sample(range(len(population)), 3)
    best = max(tournament, key=lambda idx: fitness_scores[idx])
    return population[best]

def genetic_algorithm(target_function):
    """
    Run the genetic algorithm.
    """
    population = initialize_population()
    for generation in range(GENERATIONS):
        fitness_scores = [fitness(ind[0], ind[1], target_function) for ind in population]
        next_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = select(population, fitness_scores)
            parent2 = select(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            next_population.extend([child1, child2])
        population = next_population
    return max(population, key=lambda ind: fitness(ind[0], ind[1], target_function))


from two_sum import two_sum

if __name__ == "__main__":
    best_test_case = genetic_algorithm(two_sum)
    print(f"Best Test Case: Input: {best_test_case[0]}, Target: {best_test_case[1]}")

