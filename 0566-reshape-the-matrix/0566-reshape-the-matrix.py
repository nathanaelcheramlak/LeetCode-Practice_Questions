class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        result = [[0] * c for _ in range(r)]
        col, row = 0, 0
        for i in range(m):
            for j in range(n):
                result[row][col] = mat[i][j]
                col += 1
                if col == c:
                    col = 0
                    row += 1

        return result