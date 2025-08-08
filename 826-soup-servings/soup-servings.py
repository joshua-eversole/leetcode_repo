class Solution:
    def soupServings(self, n: int) -> float:
        if n > 50000:
            return 1.0
        n = (n + 24) // 25
        # Pour 100 from A and 0 from B
        # Pour 75 from A and 25 from B
        # Pour 50 from A and 50 from B
        # Pour 25 from A and 75 from B

        self.probs = [0,0,0] # count of each happening
        #[0] is A before B, [1] is at the same time, [2] is B before A

        memo = {}
        def dp(a, b):
                if a <= 0 and b <= 0:
                    return 0.5
                if a <= 0:
                    return 1
                if b <= 0:
                    return 0
                if (a, b) in memo:
                    return memo[(a, b)]

                memo[(a, b)] = 0.25 * (
                    dp(a - 4, b) +
                    dp(a - 3, b - 1) +
                    dp(a - 2, b - 2) +
                    dp(a - 1, b - 3)
                )
                return memo[(a, b)]

        return dp(n, n)