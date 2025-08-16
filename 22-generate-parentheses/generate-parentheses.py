class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # First thoughts: dfs, either add ( or add )
        result = []
        # Input: string (current parentheses combo), depth (how many parentheses deep we are)
        def dfs(string, open, close):
            # Base case: if we've reached the end
            if len(string) == n*2:
                result.append(string)
                return
            
            # If we can still add a (
            if open < n:
                dfs(string + '(', open + 1, close)
            # If depth isn't 0, add a )
            if open > close:
                dfs(string + ')', open, close + 1) 
        
        dfs("", 0, 0)

        return result
            


        