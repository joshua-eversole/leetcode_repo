class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        majority =n//2
        i = 0
        target_count = 0
        while i < n and nums[i] != target: i += 1
        while i < n and nums[i] == target:
            i += 1
            target_count += 1
            if target_count > majority:
                return True
        return False

