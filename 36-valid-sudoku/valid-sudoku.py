class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subboxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == "." or cell == ",":
                    continue
                if cell in rows[r]:
                    return False
                else:
                    rows[r].add(cell)
                if cell in cols[c]:
                    return False
                else:
                    cols[c].add(cell)
                #for the subboxes, i'm going left to right then up to down, so board[4][7] would go in the 6th box. i'm going to acheive this by dividing by 3 and multiplying the row amount by 3
                subbox_index = (r//3)*3 + (c//3)
                if cell in subboxes[subbox_index]:
                    return False
                else:
                    subboxes[subbox_index].add(cell)


        return True
