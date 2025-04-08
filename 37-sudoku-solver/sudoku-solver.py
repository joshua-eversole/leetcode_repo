class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Init variables
        empty_spots = [] # keep track of every spot we need to add a number to
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)] # left * 3 + col
        
        # create the tables
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": 
                    empty_spots.append((i, j))
                else: 
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[i//3 * 3 + j//3].add(board[i][j])

        # Backtrack through each empty spot to see if it works
        def backtrack(i):
            # If we've reached the end, return True
            if i == len(empty_spots):
                return True
            row, col = empty_spots[i]
            sqr = row//3 * 3 + col//3
            # Run through str values of 1-9 and check them each
            for num in range(1, 10):
                char = str(num)
                # If we can add the value, add it, backtrack, and then remove it
                if char not in rows[row] and char not in cols[col] and char not in squares[sqr]:
                    board[row][col] = char

                    rows[row].add(char)
                    cols[col].add(char)
                    squares[sqr].add(char)

                    if backtrack(i + 1):
                        return True

                    rows[row].remove(char)
                    cols[col].remove(char)
                    squares[sqr].remove(char)
            return False

        backtrack(0)




        