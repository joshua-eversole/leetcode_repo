class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        prefix_sum = []
        i = 1
        while i <= n:
            if (n & i) != 0:
                prefix_sum.append(i * prefix_sum[-1] if prefix_sum else i)
            i <<= 1

        ans = []
        MOD = 10 ** 9 + 7

        for left, right in queries:
            if left == 0: 
                ans.append(
                prefix_sum[right] % MOD
                )
            else: 
                ans.append(
                (prefix_sum[right] // prefix_sum[left - 1]) % MOD
                )
        return ans