class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))

        result = 0
        for i, (x0, y0) in enumerate(points):
            bot = -inf
            top = y0
            for (x1, y1) in points[i + 1:]:
                if y1 <= top and y1 > bot:
                    result += 1
                    bot = y1
                    if y1 == top:
                        break
        return result 