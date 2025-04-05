class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, current_xor):
            if index == len(nums):
                return current_xor
            return dfs(index + 1, current_xor ^ nums[index]) + dfs(index + 1, current_xor)
        return dfs(0, 0)