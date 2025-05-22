class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Generate each row and add it to the result
        if numRows == 1:
            return [[1]]
        
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            last_row = result[i-1] + [0]
            print(f"last_row: {last_row}")
            row = [1 for _ in range(i+1)]
            print(f"i: {i}, row: {row}")
            for j in range(1, i):
                print(f" - j: {j}, becomes {last_row[j-1]} + {last_row[j]}")
                row[j] = last_row[j-1] + last_row[j]
            print(f"appended row: {row}")
            result.append(row)

        return result
        