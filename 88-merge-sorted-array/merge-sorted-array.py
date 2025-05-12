class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1, pointer, i2 = m  - 1, m + n - 1, n - 1
        while pointer >= 0:
            # If we've exhausted i1, just put the i2 number in
            if i1 < 0:
                nums1[pointer] = nums2[i2]
                pointer -= 1
                i2 -= 1
                continue
            # If we've exhausted i2, it should be good. return it
            if i2 < 0:
                return nums1

            # Otherwise, compare the pointers at i1 and i2 to see which one's bigger
            num1, num2 = nums1[i1], nums2[i2]
            # Put whichever one is bigger at the pointer index adn move down
            if num1 < num2:
                nums1[pointer] = nums2[i2]
                i2 -= 1
            else:
                nums1[pointer] = nums1[i1]
                i1 -= 1
            
            pointer -= 1
        return nums1
            



        """
        Do not return anything, modify nums1 in-place instead.
        """
        