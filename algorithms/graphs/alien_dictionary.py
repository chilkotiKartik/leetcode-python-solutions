"""
LeetCode 269: Alien Dictionary (Topological Sort with BFS / Kahn's Algorithm)
Time Complexity: O(C) where C is total length of all words
Space Complexity: O(1) fixed 26 alphabet nodes
"""
from collections import defaultdict, deque
from typing import List

def alienOrder(words: List[str]) -> str:
    adj = {c: set() for w in words for c in w}
    in_degree = {c: 0 for c in adj}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break

    q = deque([c for c in in_degree if in_degree[c] == 0])
    res = []
    while q:
        c = q.popleft()
        res.append(c)
        for neighbor in adj[c]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    return "".join(res) if len(res) == len(in_degree) else ""

if __name__ == "__main__":
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print("Alien Dictionary Order:", alienOrder(words))
