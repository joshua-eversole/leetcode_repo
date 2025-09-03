class Solution(object):
    def numberOfPairs(self, points):
        # Sort the points by x first, then y
        #   Ensures that all pairings will start with a top-left bottom-right option
        points.sort(key=lambda p:(p[0],-p[1]))
        pairings = 0
        # Go through each point, assuming it's alice
        for i,(alice_x, alice_y) in enumerate(points):
            # set a last_bob pointer to keep track of previously accepted bobs
            last_bob = float('-inf')
            # Look through each other point to find a possible Bob
            for bob_x, bob_y in points[i+1:]:
                # If bob is below Alice and before any other bob, then we can move the b pointer and 
                if alice_y >= bob_y > last_bob:
                    pairings += 1
                    last_bob = bob_y
        return pairings