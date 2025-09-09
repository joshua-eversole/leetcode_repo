class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        candidates.sort()

        def dp(total, i, combo):
            #Base case: We've reached the target
            if total == target:
                result.append(combo)
                return
            #Base case: We've passed the target
            if total > target or i >= n:
                return
            
            cell = candidates[i]

            #Recursive case: add the num
            dp(total + cell, i + 1, combo + [cell])

            # Recursive case: don't add the num
            while i < n and candidates[i] == cell:
                i += 1
            if i < n and candidates[i] == 5 and total == 0:
                print("here")
            dp(total, i, combo)

            
        dp(0, 0, [])
        return result
                
