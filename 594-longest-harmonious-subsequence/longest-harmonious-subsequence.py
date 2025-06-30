class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Can't think of an easier way than sorting it, but once we do it becomes easy
        nums.sort()
        l = 0
        max_len = 0
        for r in range(len(nums)):
            # slide the left pointer until the array is valid
            while nums[r] - nums[l] > 1:
                l += 1
            
            # move the right pointer
            if nums[r] - nums[l] == 1:
                max_len = max(max_len, r - l + 1)
            
        return max_len
            