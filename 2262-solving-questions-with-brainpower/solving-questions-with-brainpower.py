class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        
        # Go backwards from the last question in the array
        for i in range(n - 2, -1, -1):
            dp[i], skip = questions[i]
            # Try it it only if we can with the length of the array
            if i + skip + 1 < n:
                dp[i] += dp[i + skip + 1]
            # Always skip it
            dp[i] = max(dp[i], dp[i + 1])
        
        return dp[0]