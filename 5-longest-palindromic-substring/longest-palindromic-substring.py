class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s will always be at least 1, so worst case this is our palindrome
        result = s[0]
        self.res_len = 1
        #Input: starting l, r, and the string
        # Output: the longest palindrome we can make with that start
        def expandPalindrome(l,r,s):
            palindrome = ""
            n = len(s)
            # While we can expland and the expansion works, expand
            while l >= 0 and r < n and s[l] == s[r]:
                palindrome = s[l:r+1]
                l -= 1
                r += 1
            # Once it can't work for either reason, return what we have
            if len(palindrome) > self.res_len:
                self.res_len = len(palindrome)
                return palindrome
            return result
                

        # Let's avoid using the last since it'll never be bigger than s[0] anyways
        # We want to keep i=0 in case the longest palindrome is s[0:1]
        for i in range(len(s) - 1):
            # Odd: l and r start at the same, let's put in l for both
            result = expandPalindrome(i, i, s)
            # Even: l and r start right after each other
            result = expandPalindrome(i, i+1, s)


        return result





        