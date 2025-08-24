class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        one_in_sub = False
        max_subarray = 0
        for r, num in enumerate(nums):
            # Move l forward until there is only 
            if num != 1:
                while one_in_sub:
                    if nums[l] != 1:
                        one_in_sub = False
                    l += 1
                one_in_sub = True
            
            # find new max (no +1 because we're deleting one element)
            max_subarray = max(max_subarray, r - l) 

        return max_subarray

            