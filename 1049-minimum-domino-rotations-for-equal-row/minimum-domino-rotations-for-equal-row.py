class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Init the first domino, we're going to take the values from those and use them as our check
        possibilities = [tops[0], bottoms[0]]

        for i in range(1, len(tops)):
            # This will run either 1 or 2 times, so it's not a nested for loop per se. i could break it out, but this is cleaner imo
            for check in possibilities:
                # If the possible choice isn't the top or bottom, remove it
                possibilities[:] = [check for check in possibilities if check == tops[i] or check == bottoms[i]]

            #If we've removed both the original nums, there's no way to flip it
            if not possibilities:
                return -1
            # Otherwise, keep runningb through the for loop until we finish it
        
        #If we've reached here, we know that there is a true return value
        # Note: if both values made it, we still do the same number of flips. so just take the first value
        common_value = possibilities[0]
        tops_cnt, bottoms_cnt = 0, 0
        # Now go through every domino (including the first) and check the flip value
        for i in range(len(tops)):
            # Add it to the count value where it fits
            if tops[i] == common_value and bottoms[i] == common_value:
                continue
            elif tops[i] == common_value:
                tops_cnt += 1
            else:
                bottoms_cnt += 1
        
        #whichever value is lower is the number of flips, so return that
        return min(tops_cnt, bottoms_cnt)


            
        