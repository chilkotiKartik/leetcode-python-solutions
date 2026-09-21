"""
LeetCode 460: LFU Cache (Least Frequently Used)
O(1) time complexity for both get() and put() operations using frequency map and doubly linked lists.
"""
from collections import defaultdict

class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_tail(self) -> Node:
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}          # key -> Node
        self.freq_map = defaultdict(DLinkedList)  # freq -> DLinkedList
        self.min_freq = 0

    def _update(self, node: Node):
        freq = node.freq
        self.freq_map[freq].remove(node)
        if self.min_freq == freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update(node)
        else:
            if len(self.cache) >= self.capacity:
                evicted = self.freq_map[self.min_freq].pop_tail()
                del self.cache[evicted.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.freq_map[1].add_to_head(new_node)
            self.min_freq = 1

if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1
    lfu.put(3, 3)  # evicts key 2
    assert lfu.get(2) == -1
    assert lfu.get(3) == 3
    lfu.put(4, 4)  # evicts key 1
    assert lfu.get(1) == -1
    assert lfu.get(3) == 3
    assert lfu.get(4) == 4
    print("LFU Cache tests passed successfully!")
