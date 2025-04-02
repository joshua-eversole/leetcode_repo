class Solution(object):
    def platesBetweenCandles(self, s, queries):
        nearest_left = [-1] * len(s)
        prev = -1
        for i in range(len(s)):
            if s[i] == '|':
                prev = i
            nearest_left[i] = prev

        nearest_right = [-1] * len(s)
        prev = -1
        for i in range(len(s) -1, -1, -1):
            if s[i] == '|':
                prev = i
            nearest_right[i] = prev

        num_of_candles = [0] * len(s)
        c = 0
        for i in range(len(s)):
            if s[i] == '|':
                c += 1
            num_of_candles[i] = c

        res = []
        for a,b in queries:
            right = nearest_left[b]
            left = nearest_right[a]
            
            if left != -1 and right != -1 and left < right:
                res.append(right - left - (num_of_candles[right] - num_of_candles[left]))
            else:
                res.append(0)

        return res