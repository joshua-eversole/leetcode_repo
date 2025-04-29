class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort the interval list by end
        intervals.sort(key=lambda x: x[1])
        interval_count = 0
        old_end = -inf
        #Run through every interval
        for start, end in intervals:
            # If it doesn't overlap, make the new end date and continue
            if start >= old_end:
                old_end = end
            # If it does overlap, remove it
            else:
                interval_count += 1
        
        return interval_count



        