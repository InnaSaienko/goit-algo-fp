import numpy as np


def monte_carlo_dice(num_rolls: int = 100_000) -> dict[int, float]:
    """Simulate dice rolls and compute sum probabilities"""

    die_1 = np.random.randint(1, 7, size=num_rolls)
    die_2 = np.random.randint(1, 7, size=num_rolls)
    sums = die_1 + die_2

    counts = {s: 0 for s in range(2, 13)}
    for s in sums:
        counts[s] += 1

    probabilities = {k: (v / num_rolls) * 100 for k, v in counts.items()}
    return probabilities


def get_analytical_probabilities() -> dict[int, float]:
    counts = {s: 0 for s in range(2, 13)}
    for die_1 in range(1, 7):
        for die_2 in range(1, 7):
            counts[die_1 + die_2] += 1

    possible_outcomes = 36
    probabilities = {k: (v / possible_outcomes) * 100 for k, v in counts.items()}

    return probabilities


def print_table(probs_mc: dict, probs_an: dict) -> None:
    """Print comparison table"""

    print(f"{'Sum':>3} | {'Monte Carlo (%)':>15} | {'Analytical (%)':>15} | {'Diff (%)':>9}")
    print("-" * 55)

    for s in range(2, 13):
        mc = probs_mc[s]
        an = probs_an[s]
        diff = abs(mc - an)
        print(f"{s:>3} | {mc:>15.2f} | {an:>15.2f} | {diff:>9.4f}")


def plot_probabilities_table(counts: dict, probabilities: dict) -> None:
    pass


if __name__ == "__main__":
    probs_mc = monte_carlo_dice(100_000)
    probs_an = get_analytical_probabilities()
    print_table(probs_mc, probs_an)
