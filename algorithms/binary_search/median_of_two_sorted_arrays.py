"""
LeetCode 4: Median of Two Sorted Arrays
Find median of two sorted arrays in O(log(min(m, n))) time complexity.
"""
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2  # A partition
        j = half - i - 2  # B partition

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            # Partition is correct
            if total % 2:
                return float(min(Aright, Bright))
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

if __name__ == "__main__":
    assert findMedianSortedArrays([1, 3], [2]) == 2.0
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    print("Median of Two Sorted Arrays tests passed!")
