class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # create a monotonic stack 
        stack = [0]*(n+1)
        
        # counts the pops taken to move it down to 0
        res = 0
        # the index of the top of the stack
        top = 0

        for i, num in enumerate(nums):
            # while the current top is stil the largest, pop one value from the stack (and count it)
            while stack[top] > num:
                top -= 1
                res += 1
            # if the current top isn't the same as num, num is greater, so we push that onto the stack          
            if stack[top] != num:
                top += 1
                stack[top] = num
        
        # Return the final res count (plus the size of the remaining array)
        return res + top