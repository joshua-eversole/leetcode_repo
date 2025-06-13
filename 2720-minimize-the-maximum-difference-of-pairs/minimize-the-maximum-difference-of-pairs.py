class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Sort the arrays
        nums.sort()
        n = len(nums)
        l, r = 0, nums[-1] - nums[0]
        
        # Binary search
        while l < r:
            m = (l + r)//2

            # Try to form pairs
            count, i = 0, 1
            while i < n and count < p:
                if nums[i] - nums[i - 1] <= m:
                    count += 1
                    i += 2
                else:
                    i += 1

            if count >= p:
                r = m
            else:
                l = m + 1
        
        return l