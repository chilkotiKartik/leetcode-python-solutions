"""
LeetCode 126: Word Ladder II
Finds all shortest transformation sequences from beginWord to endWord.
Algorithm: Breadth-First Search (level-by-level) + DFS Backtracking.
"""
from collections import defaultdict, deque
from typing import List

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    word_set = set(wordList)
    if endWord not in word_set:
        return []

    adj = defaultdict(set)
    distance = {beginWord: 0}
    queue = deque([beginWord])
    found = False

    # BFS to build parent-child DAG
    while queue and not found:
        level_visited = {}
        for _ in range(len(queue)):
            curr = queue.popleft()
            curr_dist = distance[curr]

            for i in range(len(curr)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = curr[:i] + c + curr[i+1:]
                    if next_word in word_set:
                        if next_word not in distance:
                            level_visited[next_word] = curr_dist + 1
                            queue.append(next_word)
                            adj[curr].add(next_word)
                        elif distance[next_word] == curr_dist + 1:
                            adj[curr].add(next_word)
                        if next_word == endWord:
                            found = True

        for w, d in level_visited.items():
            distance[w] = d

    results = []
    def dfs(curr: str, path: List[str]):
        if curr == endWord:
            results.append(list(path))
            return
        for neighbor in adj[curr]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()

    dfs(beginWord, [beginWord])
    return results

if __name__ == "__main__":
    words = ["hot","dot","dog","lot","log","cog"]
    res = findLadders("hit", "cog", words)
    print("Word Ladder II Paths:", res)
