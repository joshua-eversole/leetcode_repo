class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominos = defaultdict(int)
        for top, bottom in dominoes:
            small = min(top, bottom)
            big = max(top, bottom)
            dominos[small, big] += 1
        pairs = 0
        for domino_cnt in dominos.values():
            print(f"adding {domino_cnt} to pairs")
            pairs += (domino_cnt * (domino_cnt - 1))//2
        return pairs