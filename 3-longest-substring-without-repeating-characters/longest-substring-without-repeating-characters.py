class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        chars = set()
        max_substring = 1
        for r, char in enumerate(s):
            while char in chars:
                chars.remove(s[l])
                l += 1
            chars.add(char)
            if l == r:
                continue
            max_substring = max(max_substring, r - l + 1)
        
        return max_substring
            


        