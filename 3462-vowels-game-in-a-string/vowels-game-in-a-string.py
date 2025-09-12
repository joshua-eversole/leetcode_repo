class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = ['a','e','i','o','u']
        vowel_cnt = 0
        for char in s:
            if char in vowels:
                vowel_cnt += 1
        
        if vowel_cnt == 0:
            return False
        
        return True