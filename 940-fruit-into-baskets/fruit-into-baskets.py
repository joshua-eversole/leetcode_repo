class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # This seems like a simple sliding window, just move the window to the right while keeping track of the max number of fruits
        
        # Step 1: Variable init
        l, r = 0, 0
        max_fruits_picked = 0
        basket = defaultdict(int) # keeps track of fruits in the 

        # Step 2: Sliding window
        while r < len(fruits):

            # Now that our window is good, put in the fruit we picked
            basket[fruits[r]] += 1

            # Start by sliding the end of the window until our window fits the parameters
            while l < r and len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1

            # Compare the max value
            max_fruits_picked = max(max_fruits_picked, r - l + 1)
            r += 1
        
        return max_fruits_picked

            

