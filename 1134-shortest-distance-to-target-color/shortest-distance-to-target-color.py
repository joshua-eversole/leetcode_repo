class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # Create a list for each of the three colors to easily search through
        hash = defaultdict(list)
        for i, color in enumerate(colors):
            hash[color].append(i)
        
        results = []

        # Now go through each query
        for i in range(len(queries)):
            target, color = queries[i]
            min_distance = len(colors)
            # If we don't have the color, we add a -1
            if color not in hash:
                min_distance = -1
            else:
                # Use binary search to quickly search the list
                color_list = hash[color]
                l, r = 0, len(color_list) - 1
                # min_distance will continually get closer to 0 the further the binary search gets
                m = 1
                # if min_distance is 0, then we don't need to continue
                while l <= r and min_distance != 0:
                    m = (l+r)//2
                    # Check min_distance against the distance from color_list[m] to the target
                    min_distance = min(min_distance, abs(target - color_list[m]))
                    # Adjust l or r to close the window
                    if target > color_list[m]:
                        l = m + 1
                    else:
                        r = m - 1
            # Add min_distance to results at the end of each run of the outer for loop
            results.append(min_distance)

        return results
                    
            
