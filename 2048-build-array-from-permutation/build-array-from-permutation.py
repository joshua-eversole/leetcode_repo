class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        #Go through each value in the new array
        for i in range(len(result)):
            result[i] = nums[nums[i]]
        return result
        