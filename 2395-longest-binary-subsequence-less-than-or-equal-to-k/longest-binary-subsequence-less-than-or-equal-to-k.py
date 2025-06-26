class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # Step 1: Count all 0s (safe to include)
        zeros = s.count('0')

        # Step 2: Initialize
        value = 0
        count = 0
        power = 0

        # Step 3: Traverse from right to left
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                # Step 4: Try adding if within k
                if power < 32:
                    value += 1 << power
                    if value > k:
                        break
                    count += 1
                    power += 1
            else:
                # Step 5: Just increment power
                power += 1

        # Step 6: Total = allowed 1s + all 0s
        return count + zeros