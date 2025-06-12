class Solution:
    # First thoughts: seems very simple, just goes through the array and compare adjacent, and don't forget the last to first
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = abs(nums[-1] - nums[0])
        for i in range(1, len(nums)):
            check = abs(nums[i] - nums[i-1])
            if max_diff < check:
                max_diff = check
        return max_diff

        