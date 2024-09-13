class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_depth = 0
        depth = 0
        for l in s:
            if l == '(':
                depth += 1
            elif l == ')':
                depth -= 1
            max_depth = max(max_depth, depth)
            
        return max_depth