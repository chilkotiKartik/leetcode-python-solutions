"""
Treap (Randomized Binary Search Tree + Heap).
Maintains BST property on keys and min-heap property on random priorities.
Average Time Complexity: O(log N) for Insert, Delete, and Search.
"""
import random
from typing import Optional

class TreapNode:
    def __init__(self, key: int):
        self.key = key
        self.priority = random.random()
        self.left: Optional['TreapNode'] = None
        self.right: Optional['TreapNode'] = None

class Treap:
    def __init__(self):
        self.root: Optional[TreapNode] = None

    def _rotate_right(self, y: TreapNode) -> TreapNode:
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _rotate_left(self, x: TreapNode) -> TreapNode:
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def insert(self, key: int):
        def _insert(node: Optional[TreapNode], key: int) -> TreapNode:
            if not node:
                return TreapNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
                if node.left.priority < node.priority:
                    node = self._rotate_right(node)
            elif key > node.key:
                node.right = _insert(node.right, key)
                if node.right.priority < node.priority:
                    node = self._rotate_left(node)
            return node

        self.root = _insert(self.root, key)

    def search(self, key: int) -> bool:
        curr = self.root
        while curr:
            if key == curr.key:
                return True
            curr = curr.left if key < curr.key else curr.right
        return False

if __name__ == "__main__":
    treap = Treap()
    for num in [50, 30, 20, 40, 70, 60, 80]:
        treap.insert(num)
    assert treap.search(20) == True
    assert treap.search(99) == False
    print("Treap operations verified successfully!")
