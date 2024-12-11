# Define the problems and their target functions

def max_subarray(nums, _):
    """Find the maximum sum of a contiguous subarray."""
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def longest_substring(s, _):
    """Find the length of the longest substring without repeating characters."""
    seen = {}
    start = max_length = 0
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length

def max_depth(root, _):
    """Find the maximum depth of a binary tree."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left, _), max_depth(root.right, _))

# Wrapper for the Binary Tree problem
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def random_tree(depth):
    """Generate a random binary tree of a given depth."""
    if depth == 0 or random.random() < 0.2:
        return None
    return TreeNode(
        val=random.randint(-100, 100),
        left=random_tree(depth - 1),
        right=random_tree(depth - 1)
    )

def fitness_with_string(test_input, target, target_function):
    """Adapt fitness function for string-based problems."""
    from coverage import Coverage
    cov = Coverage()
    cov.start()
    target_function(test_input, target)
    cov.stop()
    cov.save()
    coverage_percentage = cov.report(file=None, show_missing=False)
    return coverage_percentage

def genetic_algorithm_for_string(target_function):
    population = [
        ("".join(chr(random.randint(97, 122)) for _ in range(random.randint(5, 15))), 0)
        for _ in range(POPULATION_SIZE)
    ]
    for generation in range(GENERATIONS):
        fitness_scores = [fitness_with_string(ind[0], ind[1], target_function) for ind in population]
        next_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = select(population, fitness_scores)
            parent2 = select(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            next_population.extend([child1, child2])
        population = next_population
    return max(population, key=lambda ind: fitness_with_string(ind[0], ind[1], target_function))

# Genetic Algorithm Usage
if __name__ == "__main__":
    # Maximum Subarray
    best_test_case_max_subarray = genetic_algorithm(max_subarray)
    print(f"Max Subarray Best Test Case: Input: {best_test_case_max_subarray[0]}")

    # Longest Substring Without Repeating Characters
    best_test_case_longest_substring = genetic_algorithm_for_string(longest_substring)
    print(f"Longest Substring Best Test Case: Input: {best_test_case_longest_substring[0]}")

    # Maximum Depth of Binary Tree
    random_binary_tree = random_tree(4)  # Generate a random tree of depth 4
    best_test_case_max_depth = genetic_algorithm(lambda tree, _: max_depth(tree, _))
    print(f"Binary Tree Best Test Case: Generated Random Tree of Depth 4")
