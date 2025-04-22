class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col - 1
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        
        return False