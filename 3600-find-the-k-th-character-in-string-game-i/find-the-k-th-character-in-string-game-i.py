class Solution:
    def kthCharacter(self, k: int) -> str:
        def shift(s):
            # Shift each char forward in the alphabet, wrapping 'z' to 'a'
            # I unabashedly stole this code, fuck char orders
            return ''.join(chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in s)

        def recurse(current):
            # Base case: if the current string is long enough, return k-th character
            if len(current) >= k:
                return current[k - 1]
            # Otherwise, expand the string
            return recurse(current + shift(current))

        return recurse("a")
