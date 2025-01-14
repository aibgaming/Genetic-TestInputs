# Genetic Algorithms for Test Generation

This repository implements a Genetic Algorithm (GA) to generate effective test inputs for algorithm challenges, specifically targeting high code coverage and mutant detection. The project uses Python libraries like `coverage.py` for code coverage analysis and `MutPy` for mutation testing.

## Features

- **Genetic Algorithm Implementation**: Iteratively evolves test cases to improve test quality.
- **Code Coverage Analysis**: Leverages `coverage.py` to evaluate test input effectiveness.
- **Mutation Testing**: Uses `MutPy` to detect faults and ensure robust tests.
- **Comparison Metrics**: Includes tools to compare GA-generated tests against random and manual test inputs.

---

## Repository Contents

- **`genetic_algorithm.py`**: Main implementation of the Genetic Algorithm for test generation.
- **`two_sum.py`**: Example problem implementation (Two Sum).
- **`test_two_sum.py`**: Unit tests for the Two Sum problem.
- **`comparison_metrics.py`**: Compares the performance of GA-generated test inputs with baseline methods.
- **`.coverage`**: Coverage data generated by `coverage.py`.
- **`LICENSE`**: License file for the project.
- **`README.md`**: This documentation file.

---

## Prerequisites

Ensure you have Python 3.8+ installed along with the following libraries:

- `coverage`: For code coverage analysis.
- `MutPy`: For mutation testing.
- `unittest`: Standard Python testing framework.

Install the required libraries using pip:

```bash
pip install coverage
pip install mutpy
