class Solution:
    def trap(self, height: List[int]) -> int:
        # Two-pointer approach, 
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water_trapped = 0
        while l < r:
            # Move one of the pointers closer to the middle
            if height[l] < height[r]:
                l += 1
                if height[l] < l_max:
                    water_trapped += (l_max - height[l])
                l_max = max(l_max, height[l])   

            else:
                r -= 1
                if height[r] < r_max:
                    water_trapped += (r_max - height[r])
                r_max = max(r_max, height[r])

        return water_trapped
            
            
        