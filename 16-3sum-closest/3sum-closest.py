class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array and take the top 3 numbers as the first sum
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        difference = abs(target - closest_sum)


        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            # Two pointer on j and k to get as close to the midpoint as possible
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                # If our new triplet is smaller, make that the return result
                if difference > abs(target - total):
                    closest_sum = total
                    difference = abs(target - total)

                #If we've hit target, just return it
                if target == total:
                    return total
                
                # If we haven't, then adjust j and k to get closer to the targety
                if total < target:
                    j += 1
                else:
                    k -= 1
        
        return closest_sum
                
                

                
