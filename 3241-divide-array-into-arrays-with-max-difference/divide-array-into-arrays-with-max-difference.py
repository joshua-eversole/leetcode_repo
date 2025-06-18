class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        arr_len = n//3 # n will always be divisible by 3
        arrays = []
        i = 0
        while i < n:
            subarray = nums[i:i+3]
            if subarray[0] + k < subarray[-1]:
                return []
            arrays.append(subarray)
            i += 3
        return arrays