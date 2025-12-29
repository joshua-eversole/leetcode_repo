class Solution(object):
    def pyramidTransition(self, bottom, allowed):

        # Create a dictionary of every possible triplet
        T = collections.defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        # cache results
        seen = set()

        def solve(A):
            # Base case: if we reached the top
            if len(A) == 1: return True
            
            # memoization check
            if A in seen: return False
            seen.add(A)

            # Recursive: check all valid rows, solve them, and return true if any path works
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i = 0):
            # Base case: if the row is finished
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                # Look at the base pair and iterate through every possible block
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    
                    ans.pop() # remove the last value to keep the backtrack

        return solve(bottom)