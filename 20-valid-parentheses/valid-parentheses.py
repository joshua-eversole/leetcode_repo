class Solution:
    def isValid(self, s: str) -> bool:
        chars = []
        for char in s:
            if char == ']':
                if not chars or chars.pop() != '[':
                    return False

            elif char == ')':
                if not chars or chars.pop() != '(':
                    return False
            
            elif char == '}':
                if not chars or chars.pop() != '{':
                    return False

            else:
                chars.append(char)
            
        return len(chars) == 0



        