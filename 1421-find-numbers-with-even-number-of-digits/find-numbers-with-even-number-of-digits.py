class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digits = 0
        for num in nums:
            if (10 <= num < 100) or (1000 <= num < 10000) or 100000 <= num:
                even_digits += 1
        
        return even_digits

        