import argparse

import numpy as np
from matplotlib import pyplot as plt


def draw_tree(x, y, length, depth, max_depth):
    """Draw Pythagoras tree with recursion depth and color gradient"""

    if depth == 0:
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("depth", type=int, help="Recursion depth")
    args = parser.parse_args()
    plt.figure(figsize=(8, 8))
    draw_tree(0, 0, 1, np.pi / 2, args.depth, args.depth)
    plt.axis("equal")
    plt.axis("off")
    plt.show()