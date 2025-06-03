class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False

        #If they're equal, then we have to change a character
        if len(s) == len(t):
            differences = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    differences += 1
                    if differences > 1:
                        return False
            return differences == 1
        

        # If they're different, then we have to add/remove a character
        # Adding and removing is the same (removing an extra character is the same as adding a new one)
        # We'll do a similar thing, but two-pointer 
        longer, shorter = s, t
        if len(t) > len(s):
            longer, shorter = t, s
        l, r= 0, len(shorter)

        #Base case for where one of the strings is empty
        if len(shorter) == 0:
            return True

        while l < len(shorter) and longer[l] == shorter[l]:
            l += 1
        # Remember that if we get here, longer is one character bigger than shorter
        while r > l and longer[r] == shorter[r-1]:
            r -= 1
        return l == r

        
