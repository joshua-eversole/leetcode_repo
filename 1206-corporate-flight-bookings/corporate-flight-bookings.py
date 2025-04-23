class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Build the prefix sum
        prefix = [0] * (n + 1)
        # Add the seat changes to the prefix array
        for first, last, seats in bookings:
            prefix[first - 1] += seats
            prefix[last] -= seats

        # Now just go through and make add the previous sum to the value to get the total
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        
        return prefix[:n]
        

