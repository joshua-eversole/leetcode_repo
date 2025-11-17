class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        num_sum = sum(nums)
        if k == 0 or num_sum < 2:
            return True
        if sum(nums) > len(nums)//k:
            return False
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                i += 1
                for j in range(k):
                    if i+j < len(nums) and nums[i+j] == 1:
                        return False
                i += j
            
            i += 1

        return True
        
                    
        