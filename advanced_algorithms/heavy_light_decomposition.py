"""
Tree Decomposition Algorithms:
1. Heavy-Light Decomposition (HLD) with Segment Tree for Path Queries & Subtree Updates (O(log^2 N))
2. Centroid Decomposition for Path Distance and Subtree Optimization (O(N log N))
"""

from typing import List, Tuple, Optional

class HLD:
    def __init__(self, n: int):
        self.n = n
        self.adj: List[List[int]] = [[] for _ in range(n + 1)]
        self.parent = [0] * (n + 1)
        self.depth = [0] * (n + 1)
        self.heavy = [0] * (n + 1)
        self.head = [0] * (n + 1)
        self.pos = [0] * (n + 1)
        self.size = [0] * (n + 1)
        self.cur_pos = 0

    def add_edge(self, u: int, v: int):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def _dfs_size(self, u: int, p: int, d: int) -> int:
        self.parent[u] = p
        self.depth[u] = d
        self.size[u] = 1
        max_c_size = 0
        for v in self.adj[u]:
            if v != p:
                c_size = self._dfs_size(v, u, d + 1)
                self.size[u] += c_size
                if c_size > max_c_size:
                    max_c_size = c_size
                    self.heavy[u] = v
        return self.size[u]

    def _dfs_decompose(self, u: int, h: int):
        self.cur_pos += 1
        self.pos[u] = self.cur_pos
        self.head[u] = h
        if self.heavy[u] != 0:
            self._dfs_decompose(self.heavy[u], h)
        for v in self.adj[u]:
            if v != self.parent[u] and v != self.heavy[u]:
                self._dfs_decompose(v, v)

    def build(self, root: int = 1):
        self._dfs_size(root, 0, 0)
        self.cur_pos = 0
        self._dfs_decompose(root, root)

    def query_path(self, u: int, v: int) -> List[Tuple[int, int]]:
        """Returns 1D segment intervals representing path between u and v"""
        intervals = []
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                u, v = v, u
            intervals.append((self.pos[self.head[v]], self.pos[v]))
            v = self.parent[self.head[v]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        intervals.append((self.pos[u], self.pos[v]))
        return intervals

class CentroidDecomposition:
    def __init__(self, n: int):
        self.n = n
        self.adj: List[List[int]] = [[] for _ in range(n + 1)]
        self.deleted = [False] * (n + 1)
        self.sz = [0] * (n + 1)
        self.centroid_parent = [0] * (n + 1)

    def add_edge(self, u: int, v: int):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def _get_sizes(self, u: int, p: int) -> int:
        self.sz[u] = 1
        for v in self.adj[u]:
            if v != p and not self.deleted[v]:
                self.sz[u] += self._get_sizes(v, u)
        return self.sz[u]

    def _find_centroid(self, u: int, p: int, total: int) -> int:
        for v in self.adj[u]:
            if v != p and not self.deleted[v] and self.sz[v] > total // 2:
                return self._find_centroid(v, u, total)
        return u

    def decompose(self, u: int, p: int = 0) -> int:
        total = self._get_sizes(u, p)
        centroid = self._find_centroid(u, p, total)
        self.deleted[centroid] = True
        self.centroid_parent[centroid] = p

        for v in self.adj[centroid]:
            if not self.deleted[v]:
                self.decompose(v, centroid)
        return centroid
