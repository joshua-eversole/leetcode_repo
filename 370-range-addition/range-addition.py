class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # This is prefix sum (I RECOGNIZED IT!!), have a table with just the changes
        prefix_sum = [0] * length
        result = [0] * length
        # go through the updates andadd the start and remove the end from the prefix_sum
        for start, end, amt in updates:
            prefix_sum[start] += amt
            # HINT: Have to update the end + 1
            if end + 1 < length:
                prefix_sum[end + 1] -= amt
        
        
        # Now go through and add the value to the result array
        # remember to do the first on iteratively and then dynamically for the ret
        result[0] = prefix_sum[0]
        for i in range(1, len(prefix_sum)):
            result[i] = result[i-1] + prefix_sum[i]
        
        return result

        