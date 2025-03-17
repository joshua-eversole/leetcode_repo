class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = set()
        for num in nums:
            if num in count:
                count.remove(num)
            else:
                count.add(num)
        
        if count:
            return False
        return True