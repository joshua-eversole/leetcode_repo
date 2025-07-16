class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # First thoughts: since there's only two options (sum % 2 == 0 or sum % 2 == 1), we can just calculate the number for each one
        # Second thoughts: we can get four different subarrays for each value (all even, all odd, alternating (starts odd) and alternating (starts even)). add all those up
        # Third thought: instead of two different alternating arrays, just have one
        even, odd = [], []
        alt_even, alt_odd = [], []
        alternate = []

        def isOdd(num):
            return num % 2 == 1

        for num in nums:
            if not isOdd(num):
                # Even always added
                even.append(num)
                if not alternate or isOdd(alternate[-1]):
                    alternate.append(num)
            else:
                #Odd always added
                odd.append(num)
                if not alternate or not isOdd(alternate[-1]):
                    alternate.append(num)
            
        return max(len(even), len(odd), len(alternate))
            
            


        