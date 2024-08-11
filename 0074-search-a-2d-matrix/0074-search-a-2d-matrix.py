class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        
        while right >= left:
            mid = (right + left) // 2
            r, c = mid // col, mid % col
            mid_2d = matrix[r][c]
            
            if mid_2d > target:
                right = mid - 1
            elif mid_2d < target:
                left = mid + 1
            else:
                return True
        return False
        
                