class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # Go through each meeting, find all the gaps, then determine how to create the largest space 
        n = len(startTime)

        # Make a gaps array that holds all the gaps between meetings
        gaps = []
            # Add first gap
        gaps.append(startTime[0])
        # add all the gaps between meetings
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])
        # Add the last gap between the last meeting and the end of the event
        gaps.append(eventTime - endTime[-1])
        max_gap = 0
        # create a max_gap and use it to track the max amount of gaps allowable in the sliding window
        window = sum(gaps[:k+1])
        max_gap = window

        for i in range(k+1, len(gaps)):
            window += gaps[i] - gaps[i - (k+1)]
            max_gap = max(max_gap, window)
        
        return max_gap
