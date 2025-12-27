from collections import deque
from task4_binary_tree_from_heap import Node, draw_tree


def dfs_traversal(root: Node) -> list[Node]:
    """Depth-first traversal"""

    stack = [root]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return order


def bfs_traversal(root: Node) -> list[Node]:
    """Breadth-first traversal"""

    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return order


def generate_colors(n: int) -> list[str]:
    """Generate hex colors"""

    colors = []
    for i in range(n):
        r = int(30 + 100 * i / max(1, n - 1))
        g = int(60 + 120 * i / max(1, n - 1))
        b = 237
        colors.append(f"#{r:02x}{g:02x}{b:02x}")
    return colors


def apply_traversal_colors(nodes: list[Node]) -> None:
    """Apply colors to nodes"""

    colors = generate_colors(len(nodes))
    for node, color in zip(nodes, colors):
        node.color = color


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.right = Node(20)

    dfs_nodes = dfs_traversal(root)
    apply_traversal_colors(dfs_nodes)
    draw_tree(root, "task5_traversal_dfs.png")

    bfs_nodes = bfs_traversal(root)
    apply_traversal_colors(bfs_nodes)
    draw_tree(root, "task5_traversal_bfs.png")