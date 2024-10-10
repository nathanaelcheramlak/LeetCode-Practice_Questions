class Solution(object):
    def minRectanglesToCoverPoints(self, points, w):
        """
        :type points: List[List[int]]
        :type w: int
        :rtype: int
        """
        x = []
        for point in points:
            x.append(point[0])
            
        x.sort()
        last = -1
        rectangle = 0
        for i in x:
            if i > last:
                rectangle += 1
                last = i + w
        
        return rectangle
                
            
        