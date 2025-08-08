class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Sliding window, start at 0 and n and move in based on which one is lower
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        
        return max_area
            

        