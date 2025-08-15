class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        button_to_letters = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        result = []
        def dfs(i, combo):
            # Base case: if we've reached the end, append the combo
            if i == len(digits):
                result.append(combo)
                return
            # Otherwise, dfs with each letter
            for letter in button_to_letters[int(digits[i]) - 2]:
                dfs(i + 1, combo + letter)
        
        dfs(0, "")
        return result

            
            
            
