class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # make a set filled with all the initial 0s
        zero_row = set()
        zero_col = set()
        # also have a hash for all the 0s created after 
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r not in zero_row:
                        zero_row.add(r)
                    if c not in zero_col:
                        zero_col.add(c)
        
        #now go through rows
        for r in range(rows):
            # If r is in zero_row, set it all = 0
            if r in zero_row:
                matrix[r] = [0]*cols
            # If not, set all the c's
            else:
                for c in zero_col:
                    matrix[r][c] = 0
        


        