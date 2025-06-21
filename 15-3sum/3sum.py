class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()


        for i, num in enumerate(nums):
            # Skipping any duplicate numbers to speed up time
            if i > 0 and nums[i] == nums[i-1]:
                #print(f"continuing")
                continue
            
            j = i + 1
            k = len(nums) - 1

            # Do a two pointer and get it closer
            while j < k:
                tri_sum = nums[i] + nums[j] + nums[k]
                #print(f"{nums[i]} + {nums[j]} + {nums[k]} = {tri_sum}")
                # Since it's sorted, we can just use a normal tow pointer and hone in on the solution
                if tri_sum > 0:
                    k -= 1
                elif tri_sum < 0:
                    j += 1
                else:
                    #If it's 0, check to make sure we haven't already added it
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return result
            



        