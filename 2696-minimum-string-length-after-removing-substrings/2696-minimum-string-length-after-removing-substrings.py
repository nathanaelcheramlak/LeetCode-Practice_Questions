class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for l in s:
            if l == 'B' and stack and stack[-1] == 'A':
                stack.pop()
            elif l == 'D' and stack and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(l)
        
        return len(stack)