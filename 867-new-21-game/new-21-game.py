class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Edge cases
        if k == 0 or n >= (k + maxPts - 1):
            return 1.0
        
        # Init dp: have a probability from each number, start 0 at 1.0
        dp = [0.0] * maxPts
        dp[0] = 1.0
        
        # Var inits: sum of the existing sliding window, and the final result of the whole value
        window_sum = 1.0
        result = 0.0
        # Find out how much of the next window will be over n
        for i in range(1, n + 1):
            # get the probability that 
            probability = window_sum / maxPts

            # if we haven't reached k, add it to the window sum
            if i < k:
                window_sum += probability
            
            # otherwise, add it to the reuslt
            else:
                result += probability
            
            #
            if i >= maxPts:
                window_sum -= dp[i % maxPts]
            
            dp[i % maxPts] = probability
        
        return result
            







        

        



                
