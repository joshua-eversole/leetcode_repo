class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # Make n1 and n2 callable, and also create a counter for nums2 (the bigger of the two)
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        # 
        n2, cnt = self.nums2, self.cnt
        cnt[n2[index]] -= 1
        n2[index] += val
        cnt[n2[index]] += 1
        

    def count(self, tot: int) -> int:
        n1, cnt = self.nums1, self.cnt
        result = 0

        for num in n1:
            if (tot - num) in cnt:
                result += cnt[tot - num]
        
        return result


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)