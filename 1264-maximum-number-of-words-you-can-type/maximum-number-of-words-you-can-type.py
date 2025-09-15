class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        typed_words = 0
        for word in words:
            can_type = True
            for letter in brokenLetters:
                if can_type and letter in word:
                    can_type = False
            if can_type:
                typed_words += 1
        
        return typed_words
            