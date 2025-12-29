class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        for r in range(1, len(tri)):
            for c in range(len(tri[r])):
                left, right = float('inf'), float('inf')
                if c - 1 >= 0:
                    left = tri[r-1][c-1] 
                if c < len(tri[r-1]):
                    right = tri[r-1][c]
                tri[r][c] += min(left,right)
        
        return min(tri[-1])