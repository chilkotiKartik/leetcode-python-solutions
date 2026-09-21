"""
Knuth-Morris-Pratt (KMP) Substring Pattern Matching.
Time Complexity: O(N + M)
Space Complexity: O(M) for LPS array
"""
from typing import List

def computeLPS(pattern: str) -> List[int]:
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmpSearch(text: str, pattern: str) -> List[int]:
    if not pattern:
        return []

    lps = computeLPS(pattern)
    matches = []
    i = 0  # text index
    j = 0  # pattern index

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches

if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    indices = kmpSearch(text, pattern)
    assert indices == [10]
    print("KMP search algorithm verified successfully!")
