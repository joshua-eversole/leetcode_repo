class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set() #for pairs, just add (n1, n2) and (n2, n1) to make search easier
        seen = set()
        for num in nums:
            if (num - k) in seen:
                if (num, num - k) not in pairs and (num - k, num) not in pairs:
                    pairs.add((num - k, num))
            if (num + k) in seen:
                if (num, num + k) not in pairs and (num + k, num) not in pairs:
                    pairs.add((num, num + k))
            seen.add(num)
        return len(pairs)
