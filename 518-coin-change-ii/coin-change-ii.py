class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.combinations = 0
        memo = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        # Input:    purse: array of coins, 
        #           money: total amount of money in purse
        # Output: none
        def addCoin(i, target):
            # Base case: if we've passed amount or finished coins
            if target > amount or i >=len(coins):
                return 0

            # Base case: if we've already checked this value
            if memo[i][target] != -1:
                return memo[i][target]

            # End case: if we've reached amount exactly
            if target == amount:
                return 1

            # If we haven't reached amount, calculate taking this coin vs skipping it
            take = addCoin(i, target + coins[i])
            skip = addCoin(i + 1, target)

            memo[i][target] = take + skip
            return memo[i][target]
            
        return addCoin(0,0)
            