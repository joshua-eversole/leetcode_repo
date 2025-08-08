class Solution:
    # First thoughts: This is recursion, either bfs or dfs should work fine. i like bfs more
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Step 0: Variable init
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        seen = set()
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh_oranges_left = 0
        timer = 0
        # Step 1: Go through the array and add all the areas next to the rotting oranges to the q, and count the fresh oranges
        for row in range(rows):
            for col in range(cols):
                # Step 1.1: If the orange is rotting, add all the surrounding spots to the q
                if grid[row][col] == 2:
                    q.append((row, col))

                # Step 1.2: Count the total number of fresh oranges
                elif grid[row][col] == 1:
                    fresh_oranges_left += 1
        # Step 2: Run through each value in q, adding more values and increasing the timer each time
        while q and fresh_oranges_left > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    # Step 2.1: Ensure the new point is a fresh orange
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    # Step 2.2: Rot the orange and add it to the q
                        grid[nr][nc] = 2
                        fresh_oranges_left -= 1
                        q.append((nr, nc))
            # Step 2.3: Increment the timer
            timer += 1
        

        # Step 3: Return -1 if there are still fresh oranges, otherwise return the time

        if fresh_oranges_left > 0:
            return -1
        else:
            return timer
            