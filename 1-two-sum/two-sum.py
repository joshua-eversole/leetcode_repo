
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces = {}
        for i, num in enumerate(nums):
            indeces[target - num] = i
        
        for i, num in enumerate(nums):
            if num in indeces and i != indeces[num]:
                return [i, indeces[num]]

        
                