"""
Tarjan's Strongly Connected Components (SCC) and Bridge Detection.
Time Complexity: O(V + E)
Space Complexity: O(V)
"""
from typing import List, Dict, Set

def findCriticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    adj = {i: [] for i in range(n)}
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)

    discovery = [-1] * n
    low = [-1] * n
    time = 0
    bridges = []

    def dfs(node: int, parent: int):
        nonlocal time
        discovery[node] = low[node] = time
        time += 1

        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if discovery[neighbor] != -1:
                # Back-edge
                low[node] = min(low[node], discovery[neighbor])
            else:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                # Check bridge condition
                if low[neighbor] > discovery[node]:
                    bridges.append([node, neighbor])

    for i in range(n):
        if discovery[i] == -1:
            dfs(i, -1)

    return bridges

if __name__ == "__main__":
    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    bridges = findCriticalConnections(n, connections)
    assert bridges == [[1, 3]]
    print("Tarjan Bridge Detection verified successfully!")
