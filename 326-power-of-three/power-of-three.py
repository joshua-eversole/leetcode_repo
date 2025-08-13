class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # If negative, it must be odd. if even, it must be over 0
        can_be_even, l, r = False, 0, 20
        if n < 0:
            can_be_even = False
            l = 20
        
        while l <= r:
            m = (l+r)//2
            third = 3**m
            if third == n:
                return True
            elif third < n:
                l = m + 1
            else:
                r = m - 1
        return False
