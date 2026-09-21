"""
LeetCode 239: Sliding Window Maximum
Time Complexity: O(n)
Space Complexity: O(k)
Monotonic Decreasing Deque storing indices.
"""
from collections import deque
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    output = []
    q = deque()  # stores indices of elements in monotonically decreasing order
    l = r = 0

    while r < len(nums):
        # Pop smaller values from back of deque
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # Remove out-of-bounds indices from front
        if l > q[0]:
            q.popleft()

        # Record max once window reaches size k
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    assert maxSlidingWindow(nums, 3) == [3, 3, 5, 5, 6, 7]
    print("Sliding Window Maximum tests passed!")
