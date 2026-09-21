"""
Edmonds-Karp implementation of Ford-Fulkerson Maximum Flow Algorithm.
Time Complexity: O(V * E^2)
Space Complexity: O(V^2)
"""
from collections import deque
from typing import List

def maxFlow(capacity: List[List[int]], source: int, sink: int) -> int:
    n = len(capacity)
    residual = [row[:] for row in capacity]
    parent = [-1] * n

    def bfs() -> bool:
        for i in range(n):
            parent[i] = -1
        parent[source] = -2
        queue = deque([(source, float('inf'))])

        while queue:
            u, flow = queue.popleft()

            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    new_flow = min(flow, residual[u][v])
                    if v == sink:
                        return new_flow
                    queue.append((v, new_flow))
        return 0

    total_flow = 0
    while True:
        pushed_flow = bfs()
        if pushed_flow == 0:
            break
        total_flow += pushed_flow
        curr = sink
        while curr != source:
            prev = parent[curr]
            residual[prev][curr] -= pushed_flow
            residual[curr][prev] += pushed_flow
            curr = prev

    return total_flow

if __name__ == "__main__":
    cap = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    assert maxFlow(cap, 0, 5) == 23
    print("Edmonds-Karp Max Flow verified successfully!")
