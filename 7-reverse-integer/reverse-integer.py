class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        x = abs(x)
        reversed_num = 0
        max_num = (2**31 - 1)//10
        while x > 0:
            digit = x % 10
            x = x//10
            # make sure we don't go above the 32-bit int cap before multiplying
            if reversed_num > max_num:
                return 0
            
            reversed_num = reversed_num * 10 + digit
        
        if is_negative:
            return reversed_num * -1
        else:
            return reversed_num

