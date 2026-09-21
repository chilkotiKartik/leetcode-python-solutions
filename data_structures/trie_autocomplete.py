"""
Prefix Tree (Trie) with Prefix Autocomplete and Wildcard Search.
Time Complexity:
- Insert: O(L) where L is length of word
- Search / StartsWith: O(L)
- Autocomplete: O(P + N) where P is prefix length and N is subtree size
"""
from typing import List, Dict

class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False
        self.frequency: int = 0

class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, frequency: int = 1) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True
        node.frequency += frequency

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

    def autocomplete(self, prefix: str, limit: int = 5) -> List[str]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        results = []
        def dfs(curr_node: TrieNode, path: List[str]):
            if curr_node.is_end_of_word:
                results.append(("".join(path), curr_node.frequency))
            for char, next_node in curr_node.children.items():
                path.append(char)
                dfs(next_node, path)
                path.pop()

        dfs(node, list(prefix))
        # Sort by highest frequency, then lexicographically
        results.sort(key=lambda x: (-x[1], x[0]))
        return [word for word, _ in results[:limit]]

if __name__ == "__main__":
    trie = AutocompleteTrie()
    trie.insert("keploy", 10)
    trie.insert("kep", 5)
    trie.insert("keyboard", 8)
    trie.insert("kernel", 3)
    assert trie.autocomplete("ke") == ["keploy", "keyboard", "kep", "kernel"]
    print("Autocomplete Trie validated successfully!")
