class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vowel, has_cons = False, False
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        for char in word:
            if char.isalpha():
                if not (has_vowel and has_cons):
                    if char in vowels:
                        has_vowel = True
                    else:
                        has_cons = True
            elif not char.isdigit():
                return False
            
        return has_vowel and has_cons

