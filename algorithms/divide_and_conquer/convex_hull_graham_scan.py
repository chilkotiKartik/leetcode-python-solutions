"""
Convex Hull Graham Scan Algorithm in 2D Space.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""
from typing import List, Tuple

def crossProduct(o: Tuple[int, int], a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convexHull(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    points = sorted(set(points))
    if len(points) <= 2:
        return points

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and crossProduct(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and crossProduct(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hulls (last point of each list is first of other)
    return lower[:-1] + upper[:-1]

if __name__ == "__main__":
    pts = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    hull = convexHull(pts)
    assert (0, 0) in hull and (3, 0) in hull and (3, 3) in hull and (0, 3) in hull
    print("Convex Hull Graham Scan algorithm verified successfully!")
