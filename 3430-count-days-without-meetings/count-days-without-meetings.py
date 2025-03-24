class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        #print(meetings)
        days_free = 0
        prev_end = 0

        for i, (start, end) in enumerate(meetings):
            #print(f"Meeting {i + 1}: Start = {start}, End = {end}")
            
            # If there's a gap in the meeting days
            if start > prev_end + 1:
                gap = start - prev_end - 1
                days_free += gap
                #print(f"---Free days between meetings: {gap}, Total Free Days: {days_free}")
            
            prev_end = max(prev_end, end)  # Efficient update of `prev_end`

        # Calculate free days after the last meeting
        final_gap = max(0, days - prev_end)
        days_free += final_gap
        #print(f"Free days after last meeting: {final_gap}, Final Total Free Days: {days_free}")

        return days_free