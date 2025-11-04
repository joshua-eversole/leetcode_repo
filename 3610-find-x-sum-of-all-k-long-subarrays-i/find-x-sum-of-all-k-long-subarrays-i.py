from collections import defaultdict
from typing import List
import heapq

class Solution:
    # after getting it with sliding window, i got AI help for understanding the heapq solution. return to this in a few days
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        num_cnt = defaultdict(int)
        res = []

        def x_sum(window):
            # Sort by frequency descending, then value descending
            freq = sorted(window.items(), key=lambda item: (-item[1], -item[0]))
            freq_sum = 0
            for num, freq in freq[:x]:
                freq_sum += num * freq
            return freq_sum


        # Initialize first window
        for i in range(k):
            num_cnt[nums[i]] += 1
        res.append(x_sum(num_cnt))

        # Slide the window
        for i in range(k, len(nums)):
            remove = nums[i - k]
            num_cnt[remove] -= 1
            if num_cnt[remove] == 0:
                del num_cnt[remove]

            add = nums[i]
            num_cnt[add] += 1
            res.append(x_sum(num_cnt))

        return res
