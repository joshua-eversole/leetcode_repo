class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_amt = min(nums)
        moves = 0
        for num in nums:
            moves += num - min_amt
        return moves