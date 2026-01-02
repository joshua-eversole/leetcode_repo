class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        num_cnt = defaultdict(int)
        for num in nums:
            num_cnt[num] += 1
            if num_cnt[num] == n:
                return num
        return -1
            