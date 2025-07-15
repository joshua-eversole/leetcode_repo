class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dynamic programming isn't the ideal solution, but i'm gonna do it anyways
        n = len(s)
        if n == 1: return s
        
        # Init boolean table(
        dp=[[False for _ in range(n)] for _ in range(n)]
        result = s[0]
        res_len = 1

        for i in range(n):
            # The one letter ones are always true
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > res_len:
                        res_len = i-j+1
                        result = s[j:i+1]
        

        return result






        