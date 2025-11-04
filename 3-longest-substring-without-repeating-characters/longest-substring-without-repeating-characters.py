class Solution:
    # First thoughts, sliding window, continue to move down and remove when needed
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = set()
        max_len = 0

        for r in range(len(s)):
            char = s[r]
            while char in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_len = max(max_len, r - l + 1)
        
        return max_len


        