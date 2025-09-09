class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dp(i, amount, path):
            # Base case: we've passed the target
            if amount > target:
                return
            # Base case: we reached the target
            elif amount == target:
                res.append(path)
                return
            # Recursive case: run through each (remaining) candidate
            for cand_index in range(i, len(candidates)):
                cand = candidates[cand_index]
                dp(cand_index, amount + cand, path + [cand])  
        
        dp(0, 0, [])
        return res


