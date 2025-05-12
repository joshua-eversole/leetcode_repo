class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort the array by start date, then check to make sure if the last meeting has ended first
        intervals = sorted(intervals)
        last_end = -1
        for start, end in intervals:
            if start < last_end:
                return False
            last_end = end
        
        return True


        