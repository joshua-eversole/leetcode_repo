from typing import List
from collections import defaultdict

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        # Build a set for fast lookup
        point_set = set((x, y) for x, y in points)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x1, y1 = points[i]  # upper-left
                x2, y2 = points[j]  # lower-right

                if x1 > x2 or y1 < y2:
                    continue  # not a valid upper-left to lower-right

                # Check if any other point lies inside or on the border
                valid = True
                for x, y in point_set:
                    if (x1 <= x <= x2) and (y2 <= y <= y1) and (x, y) != (x1, y1) and (x, y) != (x2, y2):
                        valid = False
                        break

                if valid:
                    count += 1

        return count
