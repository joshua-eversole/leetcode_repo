import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        # Sort events and variable init
        events.sort()
        min_heap = [] # Tracking events by end day
        i, n = 0, len(events)
        events_attended = 0
        final_day = max(end for _, end in events)

        for day in range(1, final_day + 1):
            #Add events starting on this day to the heap, and remove events that already ended
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the first event
            if min_heap:
                heapq.heappop(min_heap)
                events_attended += 1
            # If there aren't events left, then we're done
            elif i == n:
                return events_attended
        
        return events_attended