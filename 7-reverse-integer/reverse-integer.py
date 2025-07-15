class Solution:
    def reverse(self, x: int) -> int:
        negative = 1
        if x < 0: 
            x *= -1
            negative = -1
        result = 0

        i = len(str(x)) - 1
        while i >= 0:
            digit = x % 10
            x = x//10
            result = result * 10 + digit
            i -= 1
        if result >= 2**31:
            return 0
        return result * negative


        