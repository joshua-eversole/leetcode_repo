class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_r, max_r, min_c, max_c = len(grid), 0, len(grid[0]), 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    min_r = min(min_r, r)
                    max_r = max(max_r, r)
                    min_c = min(min_c, c)
                    max_c = max(max_c, c)
            
        return (max_r - min_r + 1) * (max_c - min_c + 1)