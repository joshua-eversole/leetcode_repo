class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_letters, t_letters = [0]*26, [0]*26
        orda = ord('a')
        for i in range(len(s)):
            s_letters[ord(s[i]) - orda] += 1
            t_letters[ord(t[i]) - orda] += 1
        
        for i in range(26):
            if s_letters[i] != t_letters[i]:
                return False
        
        return True
            