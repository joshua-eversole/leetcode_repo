class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # first thoughts: dfs to scan each section of candidates, add it to the set
        result = []

        # Input: current path, num to hit
        def dfs(start, path, amt_left):
            # If we're at 0, add it to summed (if it's not there already)
            if amt_left == 0 and path not in result:
                result.append(path)
            # If we havent' passed 0 yet, then continue adding nums
            elif amt_left > 0:
                for i in range(start, len(candidates)):
                    print(f"i: {i}")
                    dfs(i, path + [candidates[i]], amt_left - candidates[i])
            # If we've already passed 0, do nothing
        
        dfs(0, [], target)
        return result
