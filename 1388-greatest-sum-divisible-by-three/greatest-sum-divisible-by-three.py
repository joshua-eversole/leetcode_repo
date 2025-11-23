class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # var inits
        dp = {}
        n = len(nums)
        
        # Input: index and modulo
        # Output: highest current num that follows the rule
        def recursion(i, mod):
            # Base case: if we've reached the end
            if i == n: 
                if mod == 0:
                    return 0 
                return -inf
            
            # If we've already memoized this
            if (i, mod) in dp: 
                return dp[(i, mod)]
            
            # Either take the number at i or skip it
            take = recursion(i + 1, (mod + nums[i]) % 3) + nums[i]
            skip = recursion(i + 1 , mod)
            ans = max(take, skip)

            # Memoize the answer for next time we see it
            dp[(i, mod)] = ans

            return ans
            
        return recursion(0,0)