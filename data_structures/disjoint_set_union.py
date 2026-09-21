"""
Disjoint Set Union (DSU) / Union-Find with Path Compression & Union by Rank.
Time Complexity: Nearly O(1) amortized - O(alpha(N)) per operation.
Space Complexity: O(N)
"""

class DisjointSetUnion:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.num_components = size

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False  # Already connected

        # Union by rank
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1

        self.num_components -= 1
        return True

    def connected(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)

if __name__ == "__main__":
    dsu = DisjointSetUnion(5)
    dsu.union(0, 1)
    dsu.union(1, 2)
    assert dsu.connected(0, 2) == True
    assert dsu.connected(0, 3) == False
    assert dsu.num_components == 3
    print("DSU / Union-Find operations validated successfully!")
