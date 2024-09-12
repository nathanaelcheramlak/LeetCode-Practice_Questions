class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for l in s:
            if l == '*' and stack:
                stack.pop()  
            else:
                stack.append(l)
        
        return "".join(stack)