class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val, lmax, rmax = 0, 0, 0
        for k in range(n):
            max_val = max(max_val, rmax * nums[k])
            rmax = max(rmax, lmax - nums[k])
            lmax = max(lmax, nums[k])
        return max_val