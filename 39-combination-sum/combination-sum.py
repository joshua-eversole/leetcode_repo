class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # this should be dynamic programming, think about the tree structure and remember it can be used an unlimited number of times (use memoization)
        memo = {}
        results = []
        candidates.sort()

        def dp(i, amt, path):
            # Base case
            if amt > target:
                return
            elif amt == target:
                path.sort()
                results.append(list(path))
            else:
                for j, cand in enumerate(candidates):
                    if j < i:
                        continue
                    path.append(cand)
                    dp(j, amt + cand, path)
                    path.pop()

    
        dp(0, 0, [])
        return results
