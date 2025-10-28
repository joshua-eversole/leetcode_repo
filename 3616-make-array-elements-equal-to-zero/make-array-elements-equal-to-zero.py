class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def process(nums, curr, step):
            nums_copy = nums[:]  
            n = len(nums_copy)
            total = sum(nums_copy)
            while total > 0:
                # if we're outside the valid area
                if curr < 0 or curr >= n:
                    return False
                # If nums[curr] is not 0, remove one and reverse
                if nums_copy[curr] != 0:
                    nums_copy[curr] -= 1
                    total -= 1
                    step *= -1
                # Take a step every time
                curr += step
            
            # If we exit the while loop without returning, we made everything 0
            return True

        valid_currs = 0
        for curr in range(len(nums)):
            if nums[curr] == 0:
                # First go left
                if process(nums, curr, -1):
                    valid_currs += 1
                # Then go right
                if process(nums, curr, 1):
                    valid_currs += 1
        return valid_currs
