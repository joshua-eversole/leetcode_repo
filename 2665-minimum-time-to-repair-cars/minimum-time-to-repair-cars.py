class Solution:
    #INPUT - ranks: list of ranks of all the mechanics, cars: total num of cars
    #OUTPUT - minimum time to repair all cars 
    def repairCars(self, ranks: List[int], cars: int) -> int:
        #binary search, this is kinda like koko eats bananas
        # find a time, figure out if all cars can be repaired. if it can, deceraswe the time. if it can't, incrase the time
        l, r =  0, min(ranks) * cars * cars

        def canBeRepaired(time):
            nonlocal cars
            repaired_cars = 0
            for repair_time in ranks:
                repaired_cars += int(sqrt(time//repair_time))
            if repaired_cars >= cars:
                return True
            return False

        while l <= r:
            m = (l+r)//2
            if canBeRepaired(m):
                r = m - 1
            else:
                l = m + 1
        return l
        


        
