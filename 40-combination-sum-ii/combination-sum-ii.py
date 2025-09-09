class Solution:
    #output should be a list of lists of ints
    #all the ints should add up to the sum
    #my first idea is to sort the array and then just go through that way
    #i could also use dynamic programming, but that might get messy
    #UPDATE: I checked the editorial just to see, they use backtracking. I don't know too much about backtracking, but I'm going to read more about it and find out
    #use a set to make sure the results are all distinct
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()

        def backtrack(path, i, combo):
            if combo == target:
                result.append(path[:])
                return
            for x in range(i, len(candidates)):
                if x > i and candidates[x] == candidates[x-1]:
                    continue
                if combo + candidates[x] > target: 
                    break #make sure it'll never start a backtrack where the target is                                less than the combo
                path.append(candidates[x])
                backtrack(path, x + 1, combo + candidates[x])
                path.pop()


        backtrack([], 0, 0)
        return result
        