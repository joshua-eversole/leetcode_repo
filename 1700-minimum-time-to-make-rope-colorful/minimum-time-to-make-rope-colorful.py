class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        #single run, get a list of all the duplicates in a row and keep the one that takes the longest to remove
        i = 0
        colorful_time = 0
        n = len(neededTime)
        while i < n:
            # skip forward until we reach the end or find a dupe
            while i < (n-1) and colors[i] != colors[i+1]:
                print(f"colors are {colors[i]} and {colors[i+1]}")
                i += 1
            # if we've reached the end, return the current colorful_time
            if i >= n-1:
                return colorful_time
            #otherwise, we've reached a dupe. continue going until it's not a dupe, keeping track of the total sum and maxvalue
            dupe_sum = neededTime[i]
            dupe_max = neededTime[i]
            while i < (n-1) and colors[i] == colors[i+1]:
                dupe_sum += neededTime[i+1]
                dupe_max = max(dupe_max, neededTime[i+1])
                i += 1
            print(f"dupe sum is {dupe_sum}, and dupe max is {dupe_max}")
            # now add the total dupe time (minus the one that takes the longest)
            colorful_time += (dupe_sum - dupe_max)
            i += 1
        # if we've exited the loop, we've finished cutting
        return colorful_time