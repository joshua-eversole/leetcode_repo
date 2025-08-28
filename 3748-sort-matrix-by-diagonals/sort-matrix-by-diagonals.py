class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # variable init
        n = len(grid)
        result = [[0 for _ in range(n)] for _ in range(n)]
        # create an array giving each starting point of the line
        # every line will go from the starting point, and then add one to both row and column until there are no more
        line_starts = []
        for i in range(n-1, 0, -1):
            line_starts.append((0,i))
        for i in range(n):
            line_starts.append((i,0))
            
        # run throguh each diagonal
        for r, c in (line_starts):
            line = []
            orig_r, orig_c = r, c
            pointer = -1
            # go through and get each value in the line
            while r < n and c < n:
                line.append(grid[r][c])
                r += 1
                c += 1
                pointer += 1
            
            # sort the list
            line.sort()
            # reverse it if it's the top right side
            if orig_c != 0:
                line = line[::-1]
            # go through the line again and add them in sorted order
            r, c = orig_r, orig_c
            while r < n and c < n:
                result[r][c] = line[pointer]
                pointer -= 1
                r += 1
                c += 1
        
        return result



        