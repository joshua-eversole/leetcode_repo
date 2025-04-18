class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_number_digits = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_number_digits += 1
        return even_number_digits

        