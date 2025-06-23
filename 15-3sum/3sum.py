class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array and init variables
        nums.sort()
        seen = set()
        n = len(nums)
        i, j, k = 0, 1, 2

        # Step 2: Go through each i value (to n-2)
        while i < (n-2):
            # Check for duplicate i's
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            two_sum = nums[i] * -1
            # Step 3: Do a 2-pointer search for j and k
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] == two_sum and (nums[i], nums[j], nums[k]) not in seen:
                    seen.add((nums[i], nums[j], nums[k]))
                    # Move j and k so we don't get this anymore
                    j += 1
                    k -= 1
                elif  nums[j] + nums[k] < two_sum:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
        return list(seen)



        