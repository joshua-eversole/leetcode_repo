class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_bottles = numBottles
        empty_bottles = numBottles
        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            max_bottles += new_bottles
            empty_bottles = new_bottles + (empty_bottles % numExchange)
        return max_bottles