class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # First thoughts: we can just sort potions, then compare them to each spell and keep track of the distance between that and the end of the array
        potions = sorted(potions)
        pot_cnt = len(potions)
        result = []

        # Use binary search to reduce the log times to logn
        for i, spell in enumerate(spells):
            l, r = 0, pot_cnt - 1
            min_potion = success/spell # min amount the potion needs to be to successfully bond with the spell (can be a decimal)
            while l <= r:
                m = (l+r)//2
                if potions[m] < min_potion:
                    l = m + 1
                else:
                    r = m - 1
            # now, m should be at the first acceptable potion
            result.append(pot_cnt - l)
        
        return result
            

                

