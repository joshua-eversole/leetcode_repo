class Solution:
    # First thoughts: for each group of the same colors, take the one with the highest time to remove, and get rid of everything else
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        min_time = 0
        color_list = list(colors)
        orig_balloon_cnt = len(color_list)
        while i < orig_balloon_cnt - 1:
            dupes = 0   
            # get a count of all the dupes
            while i < len(colors) - 1 and color_list[i] == color_list[i+1]:
                i += 1
                dupes += 1
            # If we have dupes, add all but the biggest one
            if dupes != 0:
                largest_time = 0
                for time in neededTime[i-dupes:i+1]:
                    largest_time = max(largest_time, time)
                    min_time += time
                min_time -= largest_time
            i += 1
        return min_time
            
            

        