class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        if n == 0:
            return result
        
        size = 1
        while size <= n:
            addon = result[:]
            for i, num in enumerate(addon):
                addon[i] += 1
            result.extend(addon)
            size *= 2
        return result[:n + 1]
