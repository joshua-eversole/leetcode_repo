class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = []
        n = len(intervals)
        
        # Edge case: if intervals is 0
        if len(intervals) == 0:
            return [newInterval]
        
        i = 0
        # Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            inserted.append(intervals[i])
            i += 1

        # Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        inserted.append(newInterval)

        # Add the rest of the intervals
        while i < n:
            inserted.append(intervals[i])
            i += 1

        
        return inserted

            
            
    

        