class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = len(height) - 1
        max_area = 0
        
        while p2 > p1:
            width = p2 - p1
            h = min(height[p1], height[p2])
            current_area = width * h;
            
            max_area = max(max_area, current_area)
            
            if height[p1] > height[p2]:
                p2 -= 1
            else: 
                p1 += 1
                
        return max_area
                