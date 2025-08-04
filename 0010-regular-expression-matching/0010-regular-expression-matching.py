class Solution:
    # First thoughts: . seems self-explanatory, the tough part is when to do *. My thought is to use dynamic programming and create a new run of the function every time to see
    def isMatch(self, s: str, p: str) -> bool:
        

        def dfs(i, j):
            # Base case
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j < len(p)-1 and p[j+1] == '*':
                # We either skip past the star and the previous number or we move i one to the right (this can continue as many times as we want)
                return dfs(i, j+2) or (match and dfs(i+1, j))
            
            if match:
                return dfs(i+1, j+1)
            
            return False


        return dfs(0, 0)





 
            