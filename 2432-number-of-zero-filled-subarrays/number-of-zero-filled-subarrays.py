class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result, subarrays = 0, 0

        for i, num in enumerate(nums):
            if num == 0: subarrays += 1
            else: subarrays = 0
            result += subarrays
        
        return result
        