"""
LeetCode 72: Edit Distance (Levenshtein Distance)
Time Complexity: O(M * N)
Space Complexity: O(N) using 1D row optimization
"""

def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = list(range(n + 1))

    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(dp[j], dp[j - 1], prev)
            prev = temp

    return dp[n]

if __name__ == "__main__":
    assert minDistance("horse", "ros") == 3
    assert minDistance("intention", "execution") == 5
    print("Edit Distance tests passed successfully!")
