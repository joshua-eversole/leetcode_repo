class Solution:
    # First Thoughts: i don't know if there's a faster way than dp, so I'll do that
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        answer = set()
        curr = {0}
        for x in arr:
            curr = {x | y for y in curr} | {x}
            answer |= curr
        
        return len(answer)


