class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        box_queue = []
        openable = [False] * n # Only true if we have the box and the key, and can be opened instantly
        have_box = [False] * n
        visited = [False] * n

        for box in initialBoxes:
            #We have the box, now if we have the key
            have_box[box] = True
            if status[box] == 1:
                openable[box] = True
                box_queue.append(box)
        
        #
        for i in range(n):
            if status[i] == 1:
                openable[i] = True

        total_candies = 0

        #While there are boxes to open, BFS through the queue
        while box_queue:
            #take the box out of the queue and add its candies to the total
            box_idx = box_queue.pop()
            if visited[box_idx]:
                continue
            visited[box_idx] = True
            total_candies += candies[box_idx]

            #See if we have new keys
            for key in keys[box_idx]:
                if not openable[key]:
                    openable[key] = True
                    if have_box[key] and not visited[key]:
                        box_queue.append(key)
            # Add the containedBoxes to the queue
            for box in containedBoxes[box_idx]:
                have_box[box] = True
                if openable[box] and not visited[box]:
                    box_queue.append(box)

        return total_candies
            