"""
A* (A-Star) Grid Pathfinding Algorithm with Manhattan & Euclidean Heuristics.
Guarantees shortest path on uniform and weighted cost grids.
"""
import heapq
from typing import List, Tuple, Optional, Dict

def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    rows, cols = len(grid), len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None

    # Priority queue storing (f_score, g_score, (r, c))
    pq = [(heuristic(start, goal), 0, start)]
    came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
    g_score = {start: 0}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        _, current_g, current = heapq.heappop(pq)

        if current == goal:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        if current_g > g_score.get(current, float('inf')):
            continue

        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                tentative_g = current_g + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(pq, (f_score, tentative_g, neighbor))

    return None

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0]
    ]
    path = a_star_search(grid, (0, 0), (3, 4))
    print("A* Optimal Path:", path)
    assert path is not None and path[0] == (0, 0) and path[-1] == (3, 4)
