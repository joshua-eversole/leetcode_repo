class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Init variables
        result = 0 # count of complete subarrays
        left = 0 
        all_nums = set(nums) #List of every unique num
        unique_num_cnt = len(all_nums) #count of unique nums
        window = {} #Key: num, value: frequency
        distinct_nums = 0
        # Run through each value
        for right, num in enumerate(nums):
            # Add the current element to window
            window[num] = window.get(num, 0) + 1
            # If we're adding a new value, increase distinct_nums
            if window[num] == 1:
                distinct_nums += 1

            #Run this until I don't have a complete set anymore (may not run even once)
            while distinct_nums == unique_num_cnt:
                # Add every iteration of the current array
                result += len(nums) - right

                # Remove nums at left from window
                window[nums[left]] -= 1

                #If we've removed the last of a value, we lose a distinct num
                if window[nums[left]] == 0:
                    distinct_nums -= 1
            
                #Increase left so we keep moving the window forward
                left += 1

        return result
