class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k] #start off min_heap with first k elements
        heapq.heapify(min_heap) #turn min_heap into a heap

        for i in range(k, len(nums)):
            #constantly remove the lowest element if it's smaller than the num
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap) #remove smaller element
                heapq.heappush(min_heap, nums[i]) #add new element

        return min_heap[0] #return smallest element in k
