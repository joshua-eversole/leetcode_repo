class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        know_secret = [0] * n # keep track of when the person learned the secret. we can figure out when they start spreading and when they forget based on this
        # 
        spreaders = 0
        total = 1
        # Tell the first person the secret
        know_secret[0] = 1
        for day in range(1, n):
            # Everyone who can spread starts spreading
            if day >= delay:
                spreaders += know_secret[day - delay]
            # When we reach forget, people start forgetting the secret. remove them from the totals
            if day >= forget:
                forgetters = know_secret[day - forget]
                total -= forgetters
                spreaders -= forgetters
            # learn who becomes aware of the spread today
            know_secret[day] = spreaders
            total += spreaders
        return total % (10**9 + 7)
            



