class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointer, every time you find a val increase the difference by one
        find, replace = 0, 0
        new_len = len(nums)
        while find < len(nums):
            # If we found the value, move find up once and decrease total length
            while find < len(nums) and nums[find] == val:
                find += 1
                new_len -= 1
            
            #If we've reached the end, return the value
            if find == len(nums):
                return new_len

            # If we need to replace something, then replace it
            nums[replace] = nums[find]
            
            # then increase both pointers
            find += 1
            replace += 1
        
        return new_len



