class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        for i, char in enumerate(s):
            if i >= 2 and char == s[i-1] and char == s[i-2]:
                continue
            result += char
        return result