class Solution:
    # greedy approach, take the first one that fits to try and get to the end 
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # n is len - 1 because we want to get to one before the end
        n = len(bits) - 1
        # didn't use this, but good for understanding the question
        possible_bits = [0, [0,1], [1,1]]
        i = 0
        # get all the way to the end, only increasing to two-num bits when necessary
        while i < n:
            if bits[i] == 1:
                i += 1
            i += 1
        
        return i == n

            

        
        
        
        