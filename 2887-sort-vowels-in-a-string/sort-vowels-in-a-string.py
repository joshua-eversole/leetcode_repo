class Solution:
    def sortVowels(self, s: str) -> str:
        # Leave consonants where they are, sort the vowels increasingly based on ASCII values
        # i need to search up converting a letter to and from an ascii value
        vowels = set('aeiouAEIOU')
        vowel_chars = []
        vowel_i = []

        # Collect vowels and their positions
        for i, char in enumerate(s):
            if char in vowels:
                vowel_chars.append(char)
                vowel_i.append(i)

        # Sort by ASCII value
        vowel_chars.sort(key=lambda c: ord(c))

        # Convert the string into a list so we can add things to each section
        s_list = list(s)
        for i, vowel in zip(vowel_i, vowel_chars):
            s_list[i] = vowel

        return ''.join(s_list)






