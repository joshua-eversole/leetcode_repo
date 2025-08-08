class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 0: Variable init
        nums.sort()
        result = []
        n = len(nums)
        # Step 1: Run through and get the i value
        for one in range(n):
            # Move one up to skip any duplicates
            if one > 0 and nums[one] == nums[one - 1]:
                continue
            two, three = one + 1, n - 1
            while two < three:
                three_sum = nums[one] + nums[two] + nums[three]
                # if they don't add up to 0, adjust two and three accordingly
                if three_sum > 0:
                    three -= 1
                elif three_sum < 0:
                    two += 1
                # If they do add up to zero, add it to the result and move until you get a new value for two
                else:
                    result.append([nums[one], nums[two], nums[three]])
                    two += 1
                    three -= 1
                    while two < three and nums[two] == nums[two - 1]:
                        two += 1

        return result 

        