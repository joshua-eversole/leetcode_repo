class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Two-pointer approach
        l, r = 0, 31
        while l <= r:
            m = (l+r)//2
            power = 2**m
            if power == n:
                return True
            elif power < n:
                l = m + 1
            else:
                r = m - 1
        return False
