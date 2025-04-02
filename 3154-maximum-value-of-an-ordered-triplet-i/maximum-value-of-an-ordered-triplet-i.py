class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val, three_max, two_max = 0, 0, 0
        for k in range(n):
            max_val = max(max_val, two_max * nums[k])
            two_max = max(two_max, three_max - nums[k])
            three_max = max(three_max, nums[k])
        return max_val