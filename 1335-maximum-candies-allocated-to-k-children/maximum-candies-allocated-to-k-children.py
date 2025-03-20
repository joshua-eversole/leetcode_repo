from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Test case if we can't get enough piles
        if sum(candies) < k:  
            return 0
        
        l, r = 1, max(candies)
        max_candies = 0

        while l <= r:
            m = (l + r) // 2

            total_piles = 0
            for candy in candies:
                total_piles += candy // m
            #total_piles = sum(candy // m for candy in candies)

            if total_piles >= k:
                max_candies = m
                l = m + 1
            else:
                r = m - 1

        return max_candies
