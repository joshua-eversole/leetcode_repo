class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Init variables
        result = [0] * len(nums)
        l, r = 0, len(nums) - 1

        # Run backwards through the array, so we start with the highest value and decrease
        for i in range(len(nums) - 1, -1, -1):
            # Take the bigger one, add it to the end, and move that pointer in one
            if abs(nums[l]) > abs(nums[r]):
                result[i] = nums[l] ** 2
                l += 1
            else:
                result[i] = nums[r] ** 2
                r -= 1
        
        return result