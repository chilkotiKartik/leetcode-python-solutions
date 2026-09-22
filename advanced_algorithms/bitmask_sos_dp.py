"""
Advanced Dynamic Programming:
1. Sum Over Subsets (SOS) DP in O(N * 2^N)
2. Traveling Salesperson Problem (TSP) with Bitmask State Compression
"""

from typing import List

def sum_over_subsets_dp(A: List[int], N: int) -> List[int]:
    """Computes F[mask] = sum(A[submask]) for all submasks in O(N * 2^N)"""
    F = list(A)
    for i in range(N):
        for mask in range(1 << N):
            if mask & (1 << i):
                F[mask] += F[mask ^ (1 << i)]
    return F

def tsp_bitmask(dist_matrix: List[List[int]]) -> int:
    """Finds minimal Hamiltonian cycle cost in O(N^2 * 2^N)"""
    n = len(dist_matrix)
    memo = {}

    def solve(mask: int, u: int) -> int:
        if mask == (1 << n) - 1:
            return dist_matrix[u][0]
        if (mask, u) in memo:
            return memo[(mask, u)]

        ans = float("inf")
        for v in range(n):
            if not (mask & (1 << v)):
                ans = min(ans, dist_matrix[u][v] + solve(mask | (1 << v), v))

        memo[(mask, u)] = ans
        return ans

    return solve(1, 0)
