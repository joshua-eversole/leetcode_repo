class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Step 0: Var init
        alices_turn = True

        lane_1_odds = n//2
        lane_1_evens = n//2
        if n%2 == 1:
            lane_1_odds += 1
        lane_2_odds = m//2
        lane_2_evens = m//2
        if m%2 == 1:
            lane_2_odds += 1
        
        return (lane_1_odds * lane_2_evens) + (lane_1_evens * lane_2_odds)
