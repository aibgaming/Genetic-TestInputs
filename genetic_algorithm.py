import argparse
import importlib
import random
from coverage import Coverage

# Genetic Algorithm Parameters
POPULATION_SIZE = 50
GENERATIONS = 20
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2
ARRAY_SIZE = (2, 10)
VALUE_RANGE = (-100, 100)
TARGET_RANGE = (-200, 200)

def fitness(test_input, target, target_function):
    cov = Coverage()
    cov.start()
    try:
        target_function(test_input, target)
    except Exception:
        pass
    cov.stop()
    cov.save()
    coverage_percentage = cov.report(file=None, show_missing=False)
    mutants_killed = 0  # Placeholder for MutPy integration
    return coverage_percentage + mutants_killed

def initialize_population():
    return [
        ([random.randint(*VALUE_RANGE) for _ in range(random.randint(*ARRAY_SIZE))], random.randint(*TARGET_RANGE))
        for _ in range(POPULATION_SIZE)
    ]

def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1, parent2
    split = random.randint(1, len(parent1[0]) - 1)
    child1 = (parent1[0][:split] + parent2[0][split:], parent1[1])
    child2 = (parent2[0][:split] + parent1[0][split:], parent2[1])
    return child1, child2

def mutate(individual):
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(individual[0]) - 1)
        individual[0][idx] = random.randint(*VALUE_RANGE)

def select(population, fitness_scores):
    tournament = random.sample(range(len(population)), 3)
    best = max(tournament, key=lambda idx: fitness_scores[idx])
    return population[best]

def genetic_algorithm(target_function):
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Genetic Algorithm for test input generation.")
    parser.add_argument("module", help="Module containing the target function (e.g., 'two_sum').")
    parser.add_argument("function", help="Function to test (e.g., 'two_sum').")
    args = parser.parse_args()

    module = importlib.import_module(args.module)
    target_function = getattr(module, args.function)

    best_test_case = genetic_algorithm(target_function)
    print(f"Best Test Case: Input: {best_test_case[0]}, Target: {best_test_case[1]}")
