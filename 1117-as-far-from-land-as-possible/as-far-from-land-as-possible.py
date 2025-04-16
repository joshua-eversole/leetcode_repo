class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c, 0))
        visited = set()
        max_dist = 0

        while q:
            r, c, dist = q.popleft()
            if 0 > r or 0 > c or r >= n or c >= n or (r,c) in visited:
                continue

            max_dist = dist
            visited.add((r,c))

            for nr, nc in [(1,0), (-1, 0), (0,1), (0,-1)]:
                q.append((r + nr, c + nc, dist + 1))
        if max_dist == 0:
            return -1
        return max_dist
