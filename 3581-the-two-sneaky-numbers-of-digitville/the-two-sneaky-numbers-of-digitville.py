class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Move out of digitville
        hash = {}
        res = []
        for num in nums:
            if num in hash:
                res.append(num)
            else:
                hash[num] = 1
        return res

