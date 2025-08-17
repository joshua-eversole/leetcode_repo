class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        a, max_val, min_val = 0, 0, 0

        for i in differences:
            a += i
            max_val = max(max_val, a)
            min_val = min(min_val, a)
        
        result = (upper - lower) - (max_val - min_val) + 1
        if result < 0:
            return 0
        return result