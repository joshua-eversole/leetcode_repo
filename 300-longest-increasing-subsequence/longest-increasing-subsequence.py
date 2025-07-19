class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1] * n
        for i in range(n - 1, -1, -1):
            last = nums[i]

            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    last = nums[j]
                    lis[i] = max(lis[i], lis[j] + 1)
        
        return max(lis)
            