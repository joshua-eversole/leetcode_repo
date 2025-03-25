class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        x_lines = [(r[0], r[2]) for r in rectangles]
        x_lines.sort()
        y_lines = [(r[1], r[3]) for r in rectangles]
        y_lines.sort()

        def countLines(intervals):
            count = 0
            prev_end = -1

            for start, end in intervals:
                if prev_end <= start:
                    count += 1
                prev_end = max(prev_end, end)

            return count

        if max(countLines(x_lines), countLines(y_lines)) >= 3: 
            return True
        return False

