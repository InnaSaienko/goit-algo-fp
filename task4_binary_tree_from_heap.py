import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    """Heap tree node"""

    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value
        self.color = "lightgreen"
        self.id = str(uuid.uuid4())


def heap_to_tree(heap: list[int], index: int = 0) -> Node | None:
    """Convert heap array to tree"""

    if index >= len(heap):
        return None

    node = Node(heap[index])
    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)
    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is None:
        return graph

    graph.add_node(node.id, label=node.val, color=node.color)

    if node.left:
        graph.add_edge(node.id, node.left.id)
        pos[node.left.id] = (x - 1 / 2 ** layer, y - 1)
        add_edges(graph, node.left, pos, x - 1 / 2 ** layer, y - 1, layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        pos[node.right.id] = (x + 1 / 2 ** layer, y - 1)
        add_edges(graph, node.right, pos, x + 1 / 2 ** layer, y - 1, layer + 1)

    return graph


def draw_tree(root: Node, filename: str) -> None:
    """Draw heap as tree"""

    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}

    add_edges(graph, root, pos)

    colors = [n[1]["color"] for n in graph.nodes(data=True)]
    labels = {n[0]: n[1]["label"] for n in graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos, labels=labels, node_color=colors, node_size=2500, arrows=False)
    plt.axis("equal")
    plt.axis("off")
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

    print(f"Tree saved as {filename}")


if __name__ == "__main__":
    data = [7, 3, 5, 1, 9, 8]
    heapq.heapify(data)  # binary heap

    root = heap_to_tree(data)
    draw_tree(root, "task4_binary_tree_from_heap.png")
