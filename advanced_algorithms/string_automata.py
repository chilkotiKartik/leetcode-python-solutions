"""
Advanced String Automata
1. Suffix Automaton (SAM) - Linear O(N) Minimal DFA for all substrings
2. Aho-Corasick Multi-Pattern Dictionary Matching Automaton
"""

from collections import deque
from typing import Dict, List, Optional, Tuple

class State:
    def __init__(self, length: int, link: int = -1):
        self.len = length
        self.link = link
        self.next: Dict[str, int] = {}
        self.is_clone = False

class SuffixAutomaton:
    def __init__(self):
        self.st: List[State] = [State(0, -1)]
        self.last = 0

    def extend(self, c: str):
        cur = len(self.st)
        self.st.append(State(self.st[self.last].len + 1))
        p = self.last
        while p != -1 and c not in self.st[p].next:
            self.st[p].next[c] = cur
            p = self.st[p].link

        if p == -1:
            self.st[cur].link = 0
        else:
            q = self.st[p].next[c]
            if self.st[p].len + 1 == self.st[q].len:
                self.st[cur].link = q
            else:
                clone = len(self.st)
                clone_state = State(self.st[p].len + 1, self.st[q].link)
                clone_state.next = dict(self.st[q].next)
                clone_state.is_clone = True
                self.st.append(clone_state)

                while p != -1 and self.st[p].next.get(c) == q:
                    self.st[p].next[c] = clone
                    p = self.st[p].link

                self.st[q].link = clone
                self.st[cur].link = clone
        self.last = cur

    def contains_substring(self, s: str) -> bool:
        u = 0
        for ch in s:
            if ch not in self.st[u].next:
                return False
            u = self.st[u].next[ch]
        return True

    def count_distinct_substrings(self) -> int:
        return sum(state.len - self.st[state.link].len for state in self.st[1:])

class AhoCorasickNode:
    def __init__(self):
        self.children: Dict[str, int] = {}
        self.fail: int = 0
        self.output: List[int] = []

class AhoCorasick:
    def __init__(self):
        self.trie: List[AhoCorasickNode] = [AhoCorasickNode()]

    def insert(self, pattern: str, pattern_id: int):
        u = 0
        for ch in pattern:
            if ch not in self.trie[u].children:
                self.trie[u].children[ch] = len(self.trie)
                self.trie.append(AhoCorasickNode())
            u = self.trie[u].children[ch]
        self.trie[u].output.append(pattern_id)

    def build(self):
        q = deque()
        for ch, v in self.trie[0].children.items():
            self.trie[v].fail = 0
            q.append(v)

        while q:
            u = q.popleft()
            for ch, v in self.trie[u].children.items():
                fail_u = self.trie[u].fail
                while fail_u and ch not in self.trie[fail_u].children:
                    fail_u = self.trie[fail_u].fail
                self.trie[v].fail = self.trie[fail_u].children.get(ch, 0)
                self.trie[v].output.extend(self.trie[self.trie[v].fail].output)
                q.append(v)

    def search(self, text: str) -> List[Tuple[int, int]]:
        matches = []
        u = 0
        for i, ch in enumerate(text):
            while u and ch not in self.trie[u].children:
                u = self.trie[u].fail
            u = self.trie[u].children.get(ch, 0)
            for pat_id in self.trie[u].output:
                matches.append((i, pat_id))
        return matches
