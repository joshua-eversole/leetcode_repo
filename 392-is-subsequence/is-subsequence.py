class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        s_i, t_i = 0, 0
        while t_i < len(t):
            if s_i < len(s) and t_i < len(t) and s[s_i] == t[t_i]:
                s_i += 1
            if s_i == len(s):
                return True
            t_i += 1
        return s_i == len(s)
        