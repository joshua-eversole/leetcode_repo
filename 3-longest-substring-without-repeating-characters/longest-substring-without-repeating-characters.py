class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        res = 0
        l = 0
        letters = set()
        for r in range(len(s)):
            # move up left
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            # add right
            letters.add(s[r])
            res = max(res, r - l + 1)
        return res