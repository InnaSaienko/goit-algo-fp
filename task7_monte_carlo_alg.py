def monte_carlo_dice(num_rolls: int = 100_000) -> tuple[dict, dict]:
    """Simulate dice rolls and compute sum probabilities"""

    counts = {}
    probabilities = {}
    return counts, probabilities


def print_table(probabilities: dict) -> None:
    """Print sum-probability table"""

    print(f"{'Sum':>3} | {'Probability (%)':>15}")
    print("-" * 22)
    for s in sorted(probabilities):
        print(f"{s:>3} | {probabilities[s]:>14.2f}%")


def plot_probabilities_table(counts: dict, probabilities: dict) -> None:
    pass

if __name__ == "__main__":
    counts, probabilities = monte_carlo_dice()