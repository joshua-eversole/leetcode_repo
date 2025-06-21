from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def addDirections(r, c):
            return ((r+1, c), (r, c+1), (r-1, c), (r, c-1))

        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()

        # Initialize queue with all rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # Rotten orange
                    queue.append((r, c))
                elif grid[r][c] == 1:  # Fresh orange
                    fresh_count += 1

        # If there are no fresh oranges, return 0
        if fresh_count == 0:
            return 0
        minutes = 0

        while queue:
            level_size = len(queue)  # The number of rotten oranges for this minute
            new_rotten = False  # Track if we rotted at least one new orange

            for _ in range(level_size):
                r, c = queue.popleft()
                for nr, nc in addDirections(r, c):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark orange as rotten
                        queue.append((nr, nc))
                        fresh_count -= 1
                        new_rotten = True  # At least one new orange rotted

            # Increase minutes only if at least one orange was rotted in this round
            if new_rotten:
                minutes += 1

        # If there are still fresh oranges left, return -1
        return minutes if fresh_count == 0 else -1