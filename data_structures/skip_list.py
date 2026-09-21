"""
Skip List Data Structure with Probabilistic Balancing.
Average Time Complexity: O(log N) for Search, Insert, and Delete.
Space Complexity: O(N) expected.
"""
import random
from typing import Optional, List

class SkipNode:
    def __init__(self, val: int = -1, level: int = 0):
        self.val = val
        self.forward: List[Optional['SkipNode']] = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipNode(-1, self.max_level)
        self.level = 0

    def _random_level(self) -> int:
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.header
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [None] * (self.max_level + 1)
        curr = self.header

        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr

        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.header
            self.level = lvl

        new_node = SkipNode(num, lvl)
        for i in range(lvl + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * (self.max_level + 1)
        curr = self.header

        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr

        curr = curr.forward[0]
        if not curr or curr.val != num:
            return False

        for i in range(self.level + 1):
            if update[i].forward[i] != curr:
                break
            update[i].forward[i] = curr.forward[i]

        while self.level > 0 and self.header.forward[self.level] is None:
            self.level -= 1

        return True

if __name__ == "__main__":
    sl = SkipList()
    sl.add(1)
    sl.add(2)
    sl.add(3)
    assert sl.search(0) == False
    sl.add(4)
    assert sl.search(1) == True
    assert sl.erase(0) == False
    assert sl.erase(1) == True
    assert sl.search(1) == False
    print("Skip List operations validated successfully!")
