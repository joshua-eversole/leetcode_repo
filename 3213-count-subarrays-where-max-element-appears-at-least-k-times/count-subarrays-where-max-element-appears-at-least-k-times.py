class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)
        # First thought is that it's two-pointer, but it might be a weird formula one
        max_num = max(set(nums))
        l = 0
        max_cnt = 0
        subarrays = 0
        for r, num in enumerate(nums):
            print()
            if num == max_num:
                max_cnt += 1
                while max_cnt == k:
                    # Add every subarray from r to the end of the array
                    subarrays += (length - r)
                    if nums[l] == max_num:
                        max_cnt -= 1
                    l += 1
        
        return subarrays
