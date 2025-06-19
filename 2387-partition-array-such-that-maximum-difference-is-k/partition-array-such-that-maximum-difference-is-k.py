class Solution:
    # First thoughts: 
    def partitionArray(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 1
        nums = sorted(nums)
        subsequences_needed = 0
        first = 0 # keeps track of the index of the first element in the subsequence
        for i, num in enumerate(nums):
            # Compare it to first
            if num > nums[first] + k:
                # If i is first, then it can't be done
                if i == first:
                    return -1
                # Otherwise, add one to the subsequences_needed, and reset first
                subsequences_needed += 1
                first = i
            # Otherwise, we can just move i forward since it'll exist in this subsequence

        # The plus one is for the last subsequence calculated in the for loop
        return subsequences_needed + 1
        

                


