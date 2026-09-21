"""
Persistent Data Structures
1. Persistent Segment Tree (Chairman Tree) for Range K-th Smallest Query
2. Wavelet Tree for Range Quantiles and Rank/Select Queries
"""

from typing import List, Optional

class PersistentSegTreeNode:
    def __init__(self, count: int = 0, left: Optional['PersistentSegTreeNode'] = None, right: Optional['PersistentSegTreeNode'] = None):
        self.count = count
        self.left = left
        self.right = right

class PersistentSegmentTree:
    def __init__(self, size: int):
        self.size = size
        self.roots: List[PersistentSegTreeNode] = [self._build(1, size)]

    def _build(self, l: int, r: int) -> PersistentSegTreeNode:
        node = PersistentSegTreeNode(0)
        if l == r:
            return node
        mid = (l + r) // 2
        node.left = self._build(l, mid)
        node.right = self._build(mid + 1, r)
        return node

    def insert(self, val_rank: int):
        new_root = self._update(self.roots[-1], 1, self.size, val_rank)
        self.roots.append(new_root)

    def _update(self, prev: PersistentSegTreeNode, l: int, r: int, val: int) -> PersistentSegTreeNode:
        node = PersistentSegTreeNode(prev.count + 1, prev.left, prev.right)
        if l == r:
            return node
        mid = (l + r) // 2
        if val <= mid:
            node.left = self._update(prev.left, l, mid, val)
        else:
            node.right = self._update(prev.right, mid + 1, r, val)
        return node

    def query_kth(self, left_version: int, right_version: int, k: int) -> int:
        return self._query(self.roots[left_version - 1], self.roots[right_version], 1, self.size, k)

    def _query(self, u: PersistentSegTreeNode, v: PersistentSegTreeNode, l: int, r: int, k: int) -> int:
        if l == r:
            return l
        count_left = v.left.count - u.left.count
        mid = (l + r) // 2
        if count_left >= k:
            return self._query(u.left, v.left, l, mid, k)
        return self._query(u.right, v.right, mid + 1, r, k - count_left)
