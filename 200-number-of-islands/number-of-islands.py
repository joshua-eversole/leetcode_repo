class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def isLand(row, col):
            # Base case: if we've visited it already
            if (row, col) in visited:
                return False
            
            if not (0 <= row < rows and 0 <= col < cols):
                return False
            
            # Base case: if we're not on land
            if  grid[row][col] == "0":
                return False

            visited.add((row, col))
            return True
        def dfs(row, col):
            if isLand(row, col):
                for move_row, move_col in directions:
                    dfs(row + move_row, col + move_col)


        def bfs(start_row, start_col):
            q = deque()
            q.append((start_row, start_col))
            while q:
                row, col = q.popleft()
                if isLand(row, col):
                    for move_row, move_col in directions:
                        q.append((row + move_row, col + move_col))

        
        #dfs
        for row in range(rows):
            for col in range(cols):
                # Every time we find a new un(explored island, explore it and add one to the count
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    bfs(row, col)
        return islands


        
            

        