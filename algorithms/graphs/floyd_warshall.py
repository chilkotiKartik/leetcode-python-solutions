"""
Floyd-Warshall All-Pairs Shortest Path Algorithm.
Time Complexity: O(V^3)
Space Complexity: O(V^2)
"""
from typing import List

def floydWarshall(n: int, edges: List[List[float]]) -> List[List[float]]:
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0.0

    for u, v, w in edges:
        dist[int(u)][int(v)] = float(w)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    return dist

if __name__ == "__main__":
    edges = [
        [0, 1, 5],
        [0, 3, 10],
        [1, 2, 3],
        [2, 3, 1]
    ]
    dist = floydWarshall(4, edges)
    assert dist[0][3] == 9.0  # 0 -> 1 -> 2 -> 3 (5 + 3 + 1)
    print("Floyd-Warshall algorithm validated successfully!")
