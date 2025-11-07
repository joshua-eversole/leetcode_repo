class Solution:
    def maxPower(self, stations, r: int, k: int) -> int:
        # Step 1: Compute prefix sums
        n = len(stations)
        prefix = [0]
        for x in stations:
            prefix.append(prefix[-1] + x)  # prefix[i+1] = sum(stations[0..i])

        # Step 2: Compute initial power per city (base power)
        base = [0] * n
        for i in range(n):
            L = max(0, i - r)
            R = min(n - 1, i + r)
            base[i] = prefix[R + 1] - prefix[L]  # total power affecting city i

        # Step 5: Define feasibility check function
        def can_make(target: int) -> bool:
            diff = [0] * (n + 1)  # difference array for range updates
            cur_add = 0           # cumulative extra power affecting current city
            used = 0              # total new stations used so far

            # Step 5.1: Iterate through all cities
            for i in range(n):
                cur_add += diff[i]  # apply any scheduled removals/additions
                cur_power = base[i] + cur_add

                # If current city has less than target power
                if cur_power < target:
                    need = target - cur_power
                    used += need
                    if used > k:  # exceed limit, not feasible
                        return False

                    # Place new stations greedily at farthest allowed position
                    cur_add += need
                    pos = min(n - 1, i + r)
                    end = min(n, pos + r + 1)  # where their effect stops
                    diff[end] -= need  # schedule removal after 'end'
            return True  # feasible if all cities reach at least target

        # Step 3: Set binary search bounds
        low, high = 0, sum(stations) + k
        ans = 0

        # Step 4: Binary search to find maximum possible minimum power
        while low <= high:
            mid = (low + high) // 2
            if can_make(mid):  # check if it's possible to achieve mid as min power
                ans = mid
                low = mid + 1  # try larger minimum
            else:
                high = mid - 1  # try smaller minimum

        # Step 7: Return the maximum possible minimum power
        return ans