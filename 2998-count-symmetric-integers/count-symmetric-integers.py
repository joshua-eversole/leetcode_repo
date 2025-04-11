class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # Variable init
        symmetric_ints = 0
        num = low
        while num <= high:
            # Make sure num has an even number of lens
            str_num = str(num)
            num_len = len(str_num)
            if num_len % 2 != 0:
                # If it's odd, move it to the next even (If that's too high, it'll exit the loop)           
                num = 10 ** num_len + 1
                continue

            #Divide the string in half
            half = num_len // 2
            left_sum, right_sum = 0, 0
            i = 0

            # Find both the left_sum and right_sum by grabbing each num from the string and adding it to the sum integer
            while i < half:
                left_sum += int(str_num[i])
                i += 1
            
            while i < num_len:
                right_sum += int(str_num[i])
                i += 1
            
            # Compare them to each other, if they're the same increase symmetric_ints
            if left_sum == right_sum:
                symmetric_ints += 1

            # Since it's a while loop, increase num
            num += 1

        return symmetric_ints

            
            
        