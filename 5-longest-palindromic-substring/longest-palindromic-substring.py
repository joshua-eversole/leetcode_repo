class Solution:
    # Remember to do both odd and even palindromes
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        n = len(s)

        def oddPalindrome(i):
            l, r = i - 1, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        def evenPalindrome(i, j):
            l, r = i, j
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(n-1):
            odd_pal = oddPalindrome(i)
            even_pal = evenPalindrome(i,i+1)
            if len(odd_pal) > len(res): res = odd_pal
            if len(even_pal) > len(res): res = even_pal

        return res




        