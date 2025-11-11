class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            hash[target - num] = i
        
        for i, num in enumerate(nums):
            if num in hash and hash[num] != i:
                return [i, hash[num]]
        