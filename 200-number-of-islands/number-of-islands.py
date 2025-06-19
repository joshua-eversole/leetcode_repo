class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def inBounds(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col):
            # Base case: if we've visited it already
            if (row, col) in visited:
                return
            

            visited.add((row, col))
            
            # Base case: if we're not on land
            if not inBounds(row, col) or grid[row][col] == "0":
                return
            
            
            # If this is land, add it to visited and check the neighbors
            for move_row, move_col in directions:
                dfs(row + move_row, col + move_col)

            return
        
        for row in range(rows):
            for col in range(cols):
                # Every time we find a new un(explored island, explore it and add one to the count
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)
        
        return islands
            

        