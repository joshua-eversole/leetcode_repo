class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # We shouldn't need a visited hash, since we're tracking when we've visited it when it rots
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        q = deque()
        fresh_oranges_left = 0
        # Start by finding all the rotting oranges and adding them to q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges_left +=1

        # Since we're starting with rotting oranges in the queue, add them to fresh_oranges_left
        #fresh_oranges_left += len(q)
        if fresh_oranges_left == 0:
            return 0
        
        rotting_timer = -1

        # Continually run through BFS, add fresh (soon-to-be-rotted) organges to the queue, and keep track of the time
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                # Make the orange rot
                # Find nearby fresh oranges to rot next turn
                for add_r, add_c in directions:
                    new_r, new_c = row + add_r, col + add_c
                    # Make sure it's a valid, fresh orange and add it if it is
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 2
                        fresh_oranges_left -= 1
                        print(f"rotting [{new_r}][{new_c}]")

            # If we've finished the turn, add one to the timer and reset the rotted_this_turn counter
            rotting_timer += 1
        
        if fresh_oranges_left != 0:
            return -1
        
        return rotting_timer

