class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = max(nums)
        max_len = 0
        i = 0
        while i < len(nums):
            j = i
            while i < len(nums) and nums[i] == n:
                i += 1
            max_len = max(max_len, i-j)
            i += 1
        return max_len