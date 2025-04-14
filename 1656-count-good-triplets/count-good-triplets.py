class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        def allTrue(i, j, k, a, b, c):
            return (abs(i - j) <= a and abs(j - k) <= b and abs(i - k) <= c)

        good_triplets = 0
        
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if allTrue(arr[i], arr[j], arr[k], a, b, c):
                        good_triplets += 1
        
        return good_triplets
