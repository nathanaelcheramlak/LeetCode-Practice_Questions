class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if target <= row[-1] and target >= row[0]:
                left, right = 0, len(row) - 1
                while right >= left:
                    mid = (right + left) // 2
                    if target > row[mid]:
                        left = mid + 1
                    elif target < row[mid]:
                        right = mid - 1
                    else:
                        return True
                    
        return False
                