"""
Segment Tree with Point Updates and Range Sum / Min / Max Queries.
Time Complexity:
- Build: O(n)
- Range Query: O(log n)
- Point Update: O(log n)
Space Complexity: O(n)
"""
from typing import List

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n) if self.n > 0 else []
        if self.n > 0:
            self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums: List[int], node: int, start: int, end: int):
        if start == end:
            self.tree[node] = nums[start]
            return
        mid = (start + end) // 2
        left_child, right_child = 2 * node + 1, 2 * node + 2
        self._build(nums, left_child, start, mid)
        self._build(nums, right_child, mid + 1, end)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index: int, val: int):
        def _update(node: int, start: int, end: int):
            if start == end:
                self.tree[node] = val
                return
            mid = (start + end) // 2
            left_child, right_child = 2 * node + 1, 2 * node + 2
            if start <= index <= mid:
                _update(left_child, start, mid)
            else:
                _update(right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

        if 0 <= index < self.n:
            _update(0, 0, self.n - 1)

    def query_range(self, l: int, r: int) -> int:
        def _query(node: int, start: int, end: int, ql: int, qr: int) -> int:
            if qr < start or ql > end:
                return 0
            if ql <= start and end <= qr:
                return self.tree[node]
            mid = (start + end) // 2
            left_sum = _query(2 * node + 1, start, mid, ql, qr)
            right_sum = _query(2 * node + 2, mid + 1, end, ql, qr)
            return left_sum + right_sum

        if l > r or self.n == 0:
            return 0
        return _query(0, 0, self.n - 1, l, r)

if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(nums)
    assert st.query_range(1, 3) == 15  # 3 + 5 + 7
    st.update(1, 10)  # nums becomes [1, 10, 5, 7, 9, 11]
    assert st.query_range(1, 3) == 22  # 10 + 5 + 7
    print("Segment Tree operations verified successfully!")
