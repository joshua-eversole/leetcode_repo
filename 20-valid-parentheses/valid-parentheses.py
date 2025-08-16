class Solution:
    def isValid(self, s: str) -> bool:
        chars = []
        brackets = {')': '(', ']':'[', '}':'{'}
        for char in s:
            if char in brackets:
                if not chars or chars.pop() != brackets[char]:
                    return False
            
            else:
                chars.append(char)
        
        return not chars
            



        