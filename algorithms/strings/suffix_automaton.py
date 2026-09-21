"""
Suffix Automaton (SAM) - Directed Acyclic Word Graph (DAWG).
Linear Time & Space Construction O(N) for string indexing and distinct substring counting.
"""
from typing import Dict, Optional

class State:
    def __init__(self, length: int = 0, link: int = -1):
        self.len = length
        self.link = link
        self.next: Dict[str, int] = {}

class SuffixAutomaton:
    def __init__(self):
        self.st: list[State] = [State(0, -1)]
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
                self.st.append(clone_state)

                while p != -1 and self.st[p].next.get(c) == q:
                    self.st[p].next[c] = clone
                    p = self.st[p].link

                self.st[q].link = clone
                self.st[cur].link = clone

        self.last = cur

    def count_distinct_substrings(self) -> int:
        total = 0
        for i in range(1, len(self.st)):
            total += self.st[i].len - self.st[self.st[i].link].len
        return total

if __name__ == "__main__":
    sam = SuffixAutomaton()
    s = "abacaba"
    for ch in s:
        sam.extend(ch)
    # Distinct substrings for 'abacaba': 21
    assert sam.count_distinct_substrings() == 21
    print("Suffix Automaton validated successfully!")
