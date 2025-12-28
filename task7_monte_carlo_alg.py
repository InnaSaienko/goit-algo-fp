import numpy as np
from matplotlib import pyplot as plt


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


def plot_probabilities_table(monte_carlo: dict[int, float], analytical: dict[int, float], filename: str) -> None:
    """Plot Monte Carlo vs analytical probabilities"""

    sums = list(range(2, 13))
    mc_values = [monte_carlo[s] for s in sums]
    an_values = [analytical[s] for s in sums]

    plt.figure(figsize=(8, 5))
    plt.plot(mc_values, sums, marker="o", color="blue", label="Monte Carlo")
    plt.plot(an_values, sums, marker="o", color="red", label="Analytical")

    plt.xlabel("Probability (%)")
    plt.ylabel("Sum of two dice")
    plt.title("Monte Carlo vs Analytical probabilities")
    plt.legend()
    plt.grid(True)

    plt.savefig(filename, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    probs_mc = monte_carlo_dice(100_000)
    probs_an = get_analytical_probabilities()
    print_table(probs_mc, probs_an)
    plot_probabilities_table(probs_mc, probs_an, "task7_monte_carlo.png")

