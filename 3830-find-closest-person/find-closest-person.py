class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # z does not move ever
        x_time, y_time = abs(x-z), abs(y-z)
        if x_time < y_time:
            return 1
        elif x_time > y_time:
            return 2
        else:
            return 0

        