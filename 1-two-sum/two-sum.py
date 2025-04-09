class Solution:
    #11/29: pretty simple, need to reread the question because i forgot about not using the same number twice
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash = {}
    for i, num in enumerate(nums):
        hash[target - num] = i
    for i, num in enumerate(nums):
        if num in hash and i != hash[num]:
            return [i, hash[num]]
    
    