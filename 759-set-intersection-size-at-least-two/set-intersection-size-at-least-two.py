class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x:x[1]) # sort by end values
        prev = [-1,-1] #adjustable [start, end] of the last interval
        size = 0

        for start, end in intervals:
            # If intervals don't overlap, add two to the size and reset the prev
            if prev[0] == -1 or prev[1] < start:
                size += 2
                prev = [end - 1, end]
            
            # If intervals do overlap, only add 1 and reset the prev
            elif prev[0] < start:
                size += 1
                if prev[1] == end:
                    prev = [end - 1, end]
                else:
                    prev[0] = prev[1]
                    prev[1] = end

        return size



        