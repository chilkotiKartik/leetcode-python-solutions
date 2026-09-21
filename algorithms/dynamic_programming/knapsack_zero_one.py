"""
0/1 Knapsack Problem with 1D Space Optimization.
Time Complexity: O(N * W)
Space Complexity: O(W)
"""
from typing import List

def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)

    for w, v in zip(weights, values):
        # Iterate backwards to prevent using the same item multiple times
        for cap in range(capacity, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)

    return dp[capacity]

if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    # Optimal: weight 3 (val 4) + weight 4 (val 5) = val 9
    assert knapsack(weights, values, capacity) == 9
    print("0/1 Knapsack optimization validated successfully!")
