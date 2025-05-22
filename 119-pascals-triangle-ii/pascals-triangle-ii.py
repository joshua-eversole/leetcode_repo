class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last_row = []
        for i in range(rowIndex + 1):
            #Create first row if it doesn't exist
            if i == 0:
                last_row = [1]
                continue
            if i == 1:
                last_row = [1, 1]
                continue

            row = [1 for _ in range(i + 1)]
            for j in range(1, i):
                row[j] = last_row[j-1] + last_row[j]
            last_row = row
        return last_row
            

            
        