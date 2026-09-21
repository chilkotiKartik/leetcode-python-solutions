"""
Fenwick Tree (Binary Indexed Tree - BIT)
Time Complexity:
- Point Update: O(log N)
- Prefix Sum Query: O(log N)
- Range Sum Query: O(log N)
Space Complexity: O(N)
"""
from typing import List

class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int):
        # 1-based indexing for internal tree
        idx = index + 1
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def query_prefix(self, index: int) -> int:
        idx = index + 1
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)
        return total

    def query_range(self, left: int, right: int) -> int:
        if left > right:
            return 0
        if left == 0:
            return self.query_prefix(right)
        return self.query_prefix(right) - self.query_prefix(left - 1)

if __name__ == "__main__":
    bit = FenwickTree(6)
    nums = [1, 3, 5, 7, 9, 11]
    for i, num in enumerate(nums):
        bit.add(i, num)

    assert bit.query_range(1, 3) == 15  # 3 + 5 + 7
    bit.add(1, 7)  # nums[1] becomes 10
    assert bit.query_range(1, 3) == 22
    print("Fenwick Tree operations verified successfully!")
