class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        trapped_water = 0

        while l < r:
            # Move the smallest one in
            if height[l] < height[r]:
                l += 1
                if height[l] < l_max:
                    trapped_water += (l_max - height[l])
                else:
                    l_max = height[l]
            else:
                r -= 1
                if height[r] < r_max:
                    trapped_water += (r_max - height[r])
                else:
                    r_max = height[r]

        return trapped_water
            
        