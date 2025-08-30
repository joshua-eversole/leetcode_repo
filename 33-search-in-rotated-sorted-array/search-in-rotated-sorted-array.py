class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Use binary search to find the number, checking to see if we're on the rotated part of the array
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l)//2
            # If nums[m] is the target, return m
            for i in [m, l, r]:
                if nums[i] == target:
                    return i

            # If the left side is sorted correctly
            if nums[m] >= nums[l]:
                # Find which half it's i, and adjust accordingly
                if nums[l] < target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            else:
                # if it's not sorted, then we have to flip our logic
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


