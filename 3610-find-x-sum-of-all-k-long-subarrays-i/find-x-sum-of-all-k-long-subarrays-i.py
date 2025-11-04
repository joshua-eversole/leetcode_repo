class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # Find the x most frequent elements
        num_cnt = defaultdict(int)
        res = []

        # Purpose: do the x_sum calculations and return the sum of the x most frequent values
        def x_sum(window):
            # i didn't do this correctly, i couldn't understand the dict to pairs
            freq = sorted([(count, num) for num, count in window.items()], reverse=True)
            freq_sum = 0
            for i, num in freq[:x]:
                if i == 0:
                    break
                freq_sum += num*i
            
            return freq_sum


        # Get the initial num_cnt and window_sum for res[0]
        for i in range(k):
            num_cnt[nums[i]] += 1
        # Add the first result
        res.append(x_sum(num_cnt))


        # Now go through the rest of the array and use sliding window to keep the num_cnt accurate
        for i in range(k, len(nums)):
            # remove the hanging num
            remove = nums[i-k]
            num_cnt[remove] -= 1
            # remove 0-count values
            if num_cnt[remove] == 0:
                del num_cnt[remove]

            # add the new num
            add = nums[i]
            num_cnt[add] += 1
            res.append(x_sum(num_cnt))
        return res

        



