class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Two-pointer approach
        return n>0 and (n & (n-1) == 0)
