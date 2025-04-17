class Solution:
    #4/17
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if i * j == 0 or (i * j) % k == 0:
                        pairs += 1
        
        return pairs

        