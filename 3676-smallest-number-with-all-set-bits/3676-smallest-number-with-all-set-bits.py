class Solution:
    def smallestNumber(self, n: int) -> int:
        # find the number of bits for n
        bits = 1
        while n > 1:
            n = n//2
            bits += 1
        
        result = 0
        while bits > 0:
            result = result * 2 + 1
            bits -= 1
        
        return result

        #then, just *2+1 the entire way until we reach it