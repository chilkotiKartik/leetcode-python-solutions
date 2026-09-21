"""
Kruskal's Minimum Spanning Tree (MST) using Disjoint Set Union (DSU).
Time Complexity: O(E log E) sorting edges
Space Complexity: O(V + E)
"""
from typing import List, Tuple

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            return False
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        return True

def kruskalMST(n: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, List[Tuple[int, int, int]]]:
    # edges format: (u, v, weight)
    edges.sort(key=lambda x: x[2])
    dsu = DSU(n)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break

    return total_weight, mst

if __name__ == "__main__":
    n = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    cost, mst = kruskalMST(n, edges)
    assert cost == 19  # (2,3,4) + (0,3,5) + (0,1,10)
    print("Kruskal MST validated successfully!")
