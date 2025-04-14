class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        res = 1
        for i in range(N):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                slope = float('inf')
                if x1 != x2:
                    slope = (y2 - y1) / (x2 - x1)
                slopes[slope] += 1
                res = max(res, slopes[slope] + 1)

        return res