"""
Travelling Salesman Problem (TSP) using Held-Karp Bitmask Dynamic Programming.
Time Complexity: O(N^2 * 2^N)
Space Complexity: O(N * 2^N)
"""
from typing import List

def tspHeldKarp(dist_matrix: List[List[float]]) -> float:
    n = len(dist_matrix)
    if n <= 1:
        return 0.0

    memo = {}

    def solve(mask: int, u: int) -> float:
        # If all cities have been visited, return distance back to starting city (city 0)
        if mask == (1 << n) - 1:
            return dist_matrix[u][0]

        state = (mask, u)
        if state in memo:
            return memo[state]

        min_cost = float('inf')
        for v in range(n):
            if not (mask & (1 << v)):
                cost = dist_matrix[u][v] + solve(mask | (1 << v), v)
                min_cost = min(min_cost, cost)

        memo[state] = min_cost
        return min_cost

    # Start at city 0 (mask = 1)
    return solve(1, 0)

if __name__ == "__main__":
    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    # Optimal cycle: 0 -> 1 -> 3 -> 2 -> 0 = 10 + 25 + 30 + 15 = 80
    assert tspHeldKarp(matrix) == 80.0
    print("Held-Karp TSP validated successfully!")
