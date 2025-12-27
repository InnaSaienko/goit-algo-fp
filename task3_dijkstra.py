import heapq


def dijkstra(graph: dict[str, dict[str, int]], start: str) -> dict[str, float]:
    """Dijkstra shortest paths with heap"""

    distances = {v: float("inf") for v in graph}
    distances[start] = 0

    heap: list[tuple[int, str]] = [(0, start)]

    while heap:
        current_dist, vertex = heapq.heappop(heap)

        if current_dist > distances[vertex]:
            continue

        for neighbor, weight in graph[vertex].items():
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2},
        "E": {"C": 10, "D": 2},
    }

    result = dijkstra(graph, "A")
    print("Shortest paths from A:")
    for node, dist in result.items():
        print(f"{node}: {dist}")
