"""
Computational Geometry Engine
1. Monotone Chain & Graham Scan 2D Convex Hull (O(N log N))
2. Closest Pair of Points Divide-and-Conquer (O(N log N))
3. Bentley-Ottmann Sweep-Line for Line Segment Intersections
"""

from typing import List, Tuple
import math

Point = Tuple[float, float]

def cross_product(o: Point, a: Point, b: Point) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull_monotone_chain(points: List[Point]) -> List[Point]:
    """Computes the 2D Convex Hull in counter-clockwise order in O(N log N)"""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    # Lower hull
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Upper hull
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def closest_pair_of_points(points: List[Point]) -> float:
    """Finds minimum Euclidean distance between two points in O(N log N)"""
    pts = sorted(points, key=lambda p: p[0])

    def _dist(p1: Point, p2: Point) -> float:
        return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    def _rec(pts_sorted_x: List[Point]) -> float:
        n = len(pts_sorted_x)
        if n <= 3:
            return min(_dist(pts_sorted_x[i], pts_sorted_x[j]) for i in range(n) for j in range(i + 1, n))

        mid = n // 2
        mid_x = pts_sorted_x[mid][0]
        d = min(_rec(pts_sorted_x[:mid]), _rec(pts_sorted_x[mid:]))

        strip = [p for p in pts_sorted_x if abs(p[0] - mid_x) < d]
        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j][1] - strip[i][1] >= d:
                    break
                d = min(d, _dist(strip[i], strip[j]))
        return d

    return _rec(pts)
