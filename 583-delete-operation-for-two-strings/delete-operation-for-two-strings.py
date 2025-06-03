class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range (m + 1)]

        # Create the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If it's the same, add one to the last max
                if word1[i-1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                #Otherwise, take the existing max
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # The last value in the table will automatically hold the Longest Common Substring

        # We return each len minus the len of the substring
        return m + n - 2 * dp[-1][-1]
                
                