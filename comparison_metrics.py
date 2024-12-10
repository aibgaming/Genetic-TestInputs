# comparison_metrics.py
def compare_results(ga_results, manual_results, random_results):
    """
    Compare metrics between GA, manual, and random inputs.
    """
    metrics = {
        "Coverage (%)": {
            "GA": ga_results["coverage"],
            "Manual": manual_results["coverage"],
            "Random": random_results["coverage"]
        },
        "Mutants Killed": {
            "GA": ga_results["mutants_killed"],
            "Manual": manual_results["mutants_killed"],
            "Random": random_results["mutants_killed"]
        }
    }
    print("Comparison Metrics:")
    for metric, results in metrics.items():
        print(f"{metric}:")
        for method, value in results.items():
            print(f"  {method}: {value}")

# Example Results (populate from actual experiments)
ga_results = {"coverage": 90, "mutants_killed": 20}
manual_results = {"coverage": 75, "mutants_killed": 10}
random_results = {"coverage": 60, "mutants_killed": 5}

compare_results(ga_results, manual_results, random_results)
