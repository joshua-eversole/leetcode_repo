class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        # Go through and flip the 1 and 0s in the obstacleGrid
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1: 
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = 1
        # Erase all 1s after the first obstacle in the first row/col
        # Do the first row (going right)
        blocked = False
        for i in range(cols):
            if blocked:
                obstacleGrid[0][i] = 0
            elif obstacleGrid[0][i] == 0:
                blocked = True
        # Now do the first column (going down)
        blocked = False
        for i in range(rows):
            if blocked:
                obstacleGrid[i][0] = 0
            elif obstacleGrid[i][0] == 0:
                blocked = True

        # Now we can go through and just add the values above and below. If there's an obstacle, then that value will be zero
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] != 0:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
        
        return obstacleGrid[-1][-1]