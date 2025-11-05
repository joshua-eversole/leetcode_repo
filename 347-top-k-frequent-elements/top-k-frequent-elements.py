import heapq

class Solution:
    # 11/5: I know it's a minheap (well, maxheap) solution but i'm not great at implementing it
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First, make a hashmap of all the occurences
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # Then, make the minheap and get the k most 
        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Finally, put the results in a list and return it
        result = []
        for _, key in heap:
            result.append(key)

        
        return result
        
        


        