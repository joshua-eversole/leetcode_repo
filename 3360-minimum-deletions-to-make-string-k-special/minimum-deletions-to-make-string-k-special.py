from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # Get an array of the sorted count
        freq = sorted(Counter(word).values())
        n = len(freq)
        min_deletions = sum(freq)


        # Run through the array, using each value as the target. Try and get every other value to get k counts away. Then compare it and find the minimum 
        for i in range(n):
            # Use freq[i] as the target minimum
            target = freq[i]
            # If it's below target - k, we have to delete everything
            deletions = sum(freq[j] for j in range(i))  
            # If it's above target + k, we need to remove enough to get it to target + k
            for j in range(i + 1, n):
                if freq[j] > target + k:
                    deletions += freq[j] - (target + k)
            min_deletions = min(min_deletions, deletions)

        return min_deletions
