class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Variable inits
        l1, l2 = len(nums1), len(nums2)
        median_pnt = (l1 + l2) // 2
        result = 0
        p1, p2 = 0, 0

        # Run through the for loop until we get to the median point
        for i in range(median_pnt):
            if p1 < l1 and p2 < l2:
                if nums1[p1] < nums2[p2]:
                    result = nums1[p1]
                    p1 += 1
                else:
                    result = nums2[p2]
                    p2 += 1
            elif p1 < l1: #nums2 is finished
                result = nums1[p1]
                p1 += 1
            else: #nums1 is finished
                result = nums2[p2]
                p2 +=1
        #get the next number
        next_num = result
        if p1 == l1:
            next_num = nums2[p2]
        elif p2 == l2:
            next_num = nums1[p1]
        else:
            next_num = min(nums1[p1], nums2[p2])
        
        #if the length is odd, return the next number
        if (l1 + l2) % 2 == 1:
            result = next_num
        #if the length is even, return the average of the current and next number
        else:
            result = (result + next_num)/2
        return result


