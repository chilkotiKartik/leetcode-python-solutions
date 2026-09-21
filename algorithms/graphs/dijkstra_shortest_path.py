"""
Dijkstra's Single Source Shortest Path with Min-Heap (Priority Queue).
Time Complexity: O((V + E) log V)
Space Complexity: O(V + E)
"""
import heapq
from typing import List, Dict, Tuple

def dijkstra(n: int, edges: List[List[int]], start: int) -> Dict[int, float]:
    adj = {i: [] for i in range(n)}
    for u, v, weight in edges:
        adj[u].append((v, weight))
        adj[v].append((u, weight))

    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0.0

    # Heap contains (current_distance, node)
    pq = [(0.0, start)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        if curr_dist > distances[u]:
            continue

        for v, weight in adj[u]:
            new_dist = curr_dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return distances

if __name__ == "__main__":
    n = 5
    edges = [
        [0, 1, 4],
        [0, 2, 1],
        [2, 1, 2],
        [1, 3, 1],
        [2, 3, 5],
        [3, 4, 3]
    ]
    dist = dijkstra(n, edges, 0)
    assert dist[0] == 0.0
    assert dist[1] == 3.0  # 0 -> 2 -> 1
    assert dist[4] == 7.0  # 0 -> 2 -> 1 -> 3 -> 4
    print("Dijkstra's algorithm validated successfully!")
