class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Variable init, should all be self-explanatory
        seen = set()
        max_score = 0
        curr_sum = 0
        l = 0

        # Two-pointer approach
        for r, num in enumerate(nums):
            # move l up until r isn't in seen
            while num in seen:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            # add num to seen, then figure out max_score
            seen.add(num)
            curr_sum += num
            max_score = max(max_score, curr_sum)

        return max_score
