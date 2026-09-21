"""
Bellman-Ford Algorithm for Single-Source Shortest Path with Negative Edge Weights & Cycle Detection.
Time Complexity: O(V * E)
Space Complexity: O(V)
"""
from typing import List, Tuple, Optional

def bellmanFord(n: int, edges: List[Tuple[int, int, float]], start: int) -> Tuple[Optional[List[float]], bool]:
    # edges format: (u, v, weight)
    dist = [float('inf')] * n
    dist[start] = 0.0

    # Relax edges V - 1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycles
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    if has_negative_cycle:
        return None, True
    return dist, False

if __name__ == "__main__":
    edges = [
        (0, 1, 4.0),
        (0, 2, 5.0),
        (1, 2, -2.0),
        (2, 3, 3.0),
        (1, 3, 10.0)
    ]
    dist, neg_cycle = bellmanFord(4, edges, 0)
    assert not neg_cycle
    assert dist == [0.0, 4.0, 2.0, 5.0]
    print("Bellman-Ford algorithm validated successfully!")
