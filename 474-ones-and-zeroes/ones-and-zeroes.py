from functools import lru_cache
from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 
        chars = [(s.count('0'), s.count('1')) for s in strs]

        # key: (i, zeroes, ones), value: max size
        @lru_cache(None)

        # input: 
        # output: max size
        def dp(i, zeroes, ones):
            # Base case: if we'ver reached the end
            if i == len(strs):
                return 0

            z, o = chars[i]

            # Option 1: skip current string
            skip = dp(i + 1, zeroes, ones)

            # Option 2: pick current string (if we have space left)
            pick = -1
            if zeroes >= z and ones >= o:
                pick = 1 + dp(i + 1, zeroes - z, ones - o)
            
            return max(pick, skip)

        return dp(0, m, n)
