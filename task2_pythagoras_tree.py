import argparse

import numpy as np
from matplotlib import pyplot as plt


def draw_tree(x, y, length, angle, counter_depth, max_depth):
    """Draw Pythagoras tree with recursion depth and color gradient"""

    if counter_depth == 0:
        return

    # x, y -> beginning of branch
    # converting length and angle into final point coordinates for a line.
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    color = (counter_depth / max_depth, 0.3, 1 - counter_depth / max_depth)

    plt.plot([x, x_end], [y, y_end], color=color, linewidth=2)
    new_length = length * 0.7
    draw_tree(x_end, y_end, new_length, angle + np.pi / 6, counter_depth - 1, max_depth)
    draw_tree(x_end, y_end, new_length, angle - np.pi / 6, counter_depth - 1, max_depth)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("depth", type=int, nargs="?", default=6, help="Recursion depth")
    args = parser.parse_args()
    plt.figure(figsize=(8, 8))
    draw_tree(0, 0, 1, np.pi / 2, counter_depth=args.depth, max_depth=args.depth,)
    plt.axis("equal")
    plt.axis("off")
    plt.savefig("task2_pythagoras_tree.png", bbox_inches='tight')
    print("Tree saved as pythagoras_tree.png")