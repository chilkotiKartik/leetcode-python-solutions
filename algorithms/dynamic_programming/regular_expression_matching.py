"""
LeetCode 10: Regular Expression Matching with '.' and '*'
Dynamic Programming table approach with O(M*N) time & space complexity.
"""

def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Deal with patterns like a*, a*b*, a*b*c*
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # Zero occurrences of preceding element
                dp[i][j] = dp[i][j - 2]
                # One or more occurrences
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[m][n]

if __name__ == "__main__":
    assert isMatch("aa", "a*") == True
    assert isMatch("ab", ".*") == True
    assert isMatch("mississippi", "mis*is*p*.") == False
    print("Regular Expression Matching DP tests passed successfully!")
