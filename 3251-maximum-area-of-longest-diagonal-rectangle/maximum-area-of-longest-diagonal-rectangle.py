class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0
        for length, width in dimensions:
            diagonal = sqrt(length**2 + width**2)
            # Larger
            if diagonal > max_diagonal or (diagonal == max_diagonal and length*width > max_area):
                max_diagonal = diagonal
                max_area = length*width
        
        return max_area
