class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        layer = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            new_layer = []
            for j in range(len(triangle[i])):
                new_val = min(triangle[i][j] + layer[j], triangle[i][j] + layer[j + 1])
                new_layer.append(new_val)
            layer = new_layer
        
        return layer[0]