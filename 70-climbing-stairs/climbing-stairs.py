class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic programming
        if n == 1: return n
        # Build a memoization table
        dp = [0 for _ in range(n + 11)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
