"""
Count Inversions in an Array using Modified Merge Sort.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""
from typing import List, Tuple

def countInversions(arr: List[int]) -> int:
    def mergeSort(nums: List[int]) -> Tuple[List[int], int]:
        if len(nums) <= 1:
            return nums, 0

        mid = len(nums) // 2
        left, left_inv = mergeSort(nums[:mid])
        right, right_inv = mergeSort(nums[mid:])

        merged = []
        inversions = left_inv + right_inv
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    _, total_inv = mergeSort(arr)
    return total_inv

if __name__ == "__main__":
    arr = [8, 4, 2, 1]
    assert countInversions(arr) == 6
    assert countInversions([1, 2, 3, 4]) == 0
    print("Inversion counter validated successfully!")
