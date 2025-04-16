class Solution:
    #4/16
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        actions = {} # Key: point, Value: number of passengers added (can be negative)
        for passengers, pick_up, drop_off in trips:
            actions[pick_up] = actions.get(pick_up, 0) + passengers
            actions[drop_off] = actions.get(drop_off, 0) - passengers
        
        sorted_actions = sorted(actions.keys())

        total_passengers = 0
        for point in sorted_actions:
            print(f"point is {point}")
            adding = actions[point]
            total_passengers += adding
            if total_passengers > capacity:
                return False
        
        return True


            



        