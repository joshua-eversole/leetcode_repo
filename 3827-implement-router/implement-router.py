from collections import deque, defaultdict
import bisect


class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.packets = set() #key: [src, dest, time], value: packet
        self.counts = defaultdict(deque) #key: destination, value: list of timestamps
        self.q = deque() #ordering packets (FIFO)


    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:

        key = (source, destination, timestamp)

        # Make sure it isn't a duplicate. if it is, return False
        if key in self.packets:
            return False
        
        # add the new packet to all the inits
        self.q.append(key)
        self.counts[destination].append(timestamp)
        self.packets.add(key)

        # if we've exceeded the limit, remove the least recent one
        while len(self.q) > self.limit:
            evict = self.q.popleft()
            evict_dest = evict[1]
            self.counts[evict_dest].popleft()
            self.packets.discard(evict)
        
        # if we've added it, return true
        return True

    def forwardPacket(self) -> List[int]:
        # Ensure there is a queue
        if not self.q:
            return []

        # pop off the oldest packet and return it
        src, dest, time = self.q.popleft()
        self.counts[dest].popleft()
        self.packets.discard((src, dest, time))
        return [src, dest, time]
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # Binary search
        l = bisect.bisect_left(self.counts[destination], startTime)
        r = bisect.bisect_right(self.counts[destination], endTime)

        return r - l



# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)