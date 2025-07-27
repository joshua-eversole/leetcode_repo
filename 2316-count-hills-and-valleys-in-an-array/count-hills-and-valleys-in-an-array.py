class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 1
        hills_and_valleys = 0
        while i < len(nums) - 1:
            prev = nums[i-1]
            num = nums[i]
            while i < len(nums) - 2 and nums[i+1] == nums[i]:
                i += 1
            nxt = nums[i+1]
            if (prev < num and nxt < num) or (prev > num and nxt > num):
                hills_and_valleys += 1
            i += 1
        
        return hills_and_valleys

            

