class Solution:
    # single run through of the nums, keep track of lowest value. Every time we get a higher value, just calculate that and update max_diff. Very similar to the best time to buy and sell stock question
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        low_val = nums[0]
        for num in nums:
            # If it's a new lowest
            if num < low_val:
                low_val = num
                continue
            # If it's higher than the current lowest
            if num > low_val:
                max_diff = max(max_diff, num - low_val)

        return max_diff