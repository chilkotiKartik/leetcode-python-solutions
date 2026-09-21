"""
Longest Common Subsequence (LCS) with Space Optimization.
Time Complexity: O(M * N)
Space Complexity: O(N) using two rows
"""

def longestCommonSubsequence(text1: str, text2: str) -> int:
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = list(curr)

    return curr[n]

if __name__ == "__main__":
    assert longestCommonSubsequence("abcde", "ace") == 3
    assert longestCommonSubsequence("abc", "abc") == 3
    assert longestCommonSubsequence("abc", "def") == 0
    print("Longest Common Subsequence validated successfully!")
