class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ndl = len(needle)
        end_pnt = len(haystack) - ndl + 1
        for i in range(0, end_pnt):
            if haystack[i:i+ndl] == needle:
                return i
        return -1