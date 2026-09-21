"""
LeetCode 124: Binary Tree Maximum Path Sum
Time Complexity: O(N)
Space Complexity: O(H) recursion depth
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            current_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path)
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return int(self.max_sum)
