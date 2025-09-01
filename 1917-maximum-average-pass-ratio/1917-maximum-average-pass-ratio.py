class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Should be greedy, keep track of each class size and add an extra student to the smallest one
        def addToHeap(p, t):
            # possible gains is the benifit from adding one to each. It's the difference between adding one and not adding one
            gains = (p + 1)/(t + 1) - p/t
            # Add it to the heap (make it negative to make maxheap possible)
            heapq.heappush(heap, (gains * -1, p, t))


        # Heap in python is minheap, we need to switch to a maxheap
        heap = []

        # Run through classes and find the class size of each
        for p, t in classes:
            addToHeap(p,t)

        # For each extra student, take the class with the biggest change and add the extra student to it
        for _ in range(extraStudents):
            # Take the max difference from the heapq
            _, p, t = heapq.heappop(heap)

            #Add a passing student (+1 to pass and +1 to total)
            p += 1
            t += 1

            # Add the new ratio back to heapq
            addToHeap(p,t)

        # Now that we added the students, get the sum of the heap and divide it by the number of classes
        all_ratio = 0
        for _, p, t in heap:
            all_ratio += (p/t)

        result = all_ratio / len(classes)

        return result