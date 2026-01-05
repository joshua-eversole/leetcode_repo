class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        negative_count = 0
        min_negative = 100001
        negative_sum = 0
        positive_sum = 0
        # count all the negatives in the array
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                cell = matrix[r][c]
                if cell <= 0:
                    negative_count += 1
                    negative_sum += cell
                else:
                    positive_sum += cell
                
                # get the min_negative (closest to 0)
                min_negative = min(min_negative, abs(cell))

        
        matrix_sum = positive_sum - negative_sum

        # if it's odd, we didn't get one negative value, so change that
        if negative_count % 2 != 0:
            matrix_sum -= 2 * min_negative
        
        return matrix_sum
            
        