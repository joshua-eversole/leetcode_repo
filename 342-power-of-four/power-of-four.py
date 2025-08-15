class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        l, r = 0, 16
        while l <= r:
            m = ((l+r)//2)
            num = 4**m
            print(f"m: {m}, num: {num}")
            if n == num:
                return True
            elif n > num:
                l = m + 1
            else:
                r = m-1
        return False
        