class Solution:
    def getValue(self, mat, row, col):
        if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
            return mat[row][col]
        return inf
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dp = [[0 if mat[row][col] == 0 else inf for col in range(cols)] for row in range(rows)]

        # Go through top left to bottom right
        for row in range(rows):
            for col in range(cols):
                if dp[row][col] != 0:
                    up = self.getValue(dp, row - 1, col)
                    left = self.getValue(dp, row, col - 1)
                    dp[row][col] = min(dp[row][col], up + 1, left + 1)
                

        # Now go back through bottom right to top left
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if dp[row][col] != 0:
                    down = self.getValue(dp, row + 1, col)
                    right = self.getValue(dp, row, col + 1)
                    dp[row][col] = min(dp[row][col], down + 1, right + 1)

        return dp
                
