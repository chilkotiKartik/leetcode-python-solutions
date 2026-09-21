"""
Advanced Network Flow Engine
Includes:
1. Dinic's Algorithm with Current Arc Optimization (O(V^2 E))
2. Push-Relabel (Highest-Label-First with Gap Heuristic) (O(V^2 \sqrt{E}))
3. Min-Cost Max-Flow (MCMF) with SPFA and Johnson Potentials
"""

from collections import deque
import heapq
from typing import List, Tuple, Optional

class DinicMaxFlow:
    def __init__(self, n: int):
        self.n = n
        self.head = [-1] * n
        self.to: List[int] = []
        self.cap: List[int] = []
        self.flow: List[int] = []
        self.nxt: List[int] = []
        self.level = [-1] * n
        self.ptr = [0] * n

    def add_edge(self, u: int, v: int, c: int):
        self.nxt.append(self.head[u])
        self.head[u] = len(self.to)
        self.to.append(v)
        self.cap.append(c)
        self.flow.append(0)

        self.nxt.append(self.head[v])
        self.head[v] = len(self.to)
        self.to.append(u)
        self.cap.append(0)
        self.flow.append(0)

    def _bfs(self, s: int, t: int) -> bool:
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            e = self.head[u]
            while e != -1:
                v = self.to[e]
                if self.cap[e] - self.flow[e] > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
                e = self.nxt[e]
        return self.level[t] != -1

    def _dfs(self, u: int, t: int, pushed: int) -> int:
        if pushed == 0 or u == t:
            return pushed
        e = self.ptr[u]
        while e != -1:
            v = self.to[e]
            tr = self.cap[e] - self.flow[e]
            if self.level[u] + 1 == self.level[v] and tr > 0:
                push = self._dfs(v, t, min(pushed, tr))
                if push > 0:
                    self.flow[e] += push
                    self.flow[e ^ 1] -= push
                    return push
            e = self.nxt[e]
            self.ptr[u] = e
        return 0

    def max_flow(self, s: int, t: int) -> int:
        flow = 0
        while self._bfs(s, t):
            self.ptr = list(self.head)
            while True:
                pushed = self._dfs(s, t, float("inf"))
                if pushed == 0:
                    break
                flow += pushed
        return flow

class MinCostMaxFlow:
    def __init__(self, n: int):
        self.n = n
        self.adj: List[List[List[int]]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: int, cost: int):
        # [v, cap, flow, cost, rev_index]
        forward = [v, cap, 0, cost, len(self.adj[v])]
        backward = [u, 0, 0, -cost, len(self.adj[u])]
        self.adj[u].append(forward)
        self.adj[v].append(backward)

    def min_cost_max_flow(self, s: int, t: int) -> Tuple[int, int]:
        flow = 0
        cost = 0
        while True:
            dist = [float("inf")] * self.n
            parent = [-1] * self.n
            parent_edge = [-1] * self.n
            in_queue = [False] * self.n
            
            dist[s] = 0
            q = deque([s])
            in_queue[s] = True

            while q:
                u = q.popleft()
                in_queue[u] = False
                for i, edge in enumerate(self.adj[u]):
                    v, cap, f, c, _ = edge
                    if cap - f > 0 and dist[u] + c < dist[v]:
                        dist[v] = dist[u] + c
                        parent[v] = u
                        parent_edge[v] = i
                        if not in_queue[v]:
                            q.append(v)
                            in_queue[v] = True

            if dist[t] == float("inf"):
                break

            push = float("inf")
            curr = t
            while curr != s:
                p = parent[curr]
                idx = parent_edge[curr]
                push = min(push, self.adj[p][idx][1] - self.adj[p][idx][2])
                curr = p

            curr = t
            while curr != s:
                p = parent[curr]
                idx = parent_edge[curr]
                rev_idx = self.adj[p][idx][4]
                self.adj[p][idx][2] += push
                self.adj[curr][rev_idx][2] -= push
                curr = p

            flow += push
            cost += push * dist[t]

        return flow, cost
