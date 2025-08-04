class Solution:
    # First thoughts: . seems self-explanatory, the tough part is when to do *. My thought is to use dynamic programming and create a new run of the function every time to see
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        def dfs(i, j):
            # Base case: if we did this already
            if (i,j) in cache:
                return cache[(i,j)]
            # Base case
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j < len(p)-1 and p[j+1] == '*':
                # We either skip past the star and the previous number or we move i one to the right (this can continue as many times as we want)
                cache[(i,j)] = dfs(i, j+2) or (match and dfs(i+1, j))
                return cache[(i,j)]
            
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
            else:
                cache[(i,j)] = False
            return cache[(i,j)]


        return dfs(0, 0)





 
            