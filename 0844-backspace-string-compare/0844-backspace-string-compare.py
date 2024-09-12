class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_one = []
        stack_two = []
        
        for l in s:
            if l == "#":
                if stack_one:
                    stack_one.pop()
            else:
                stack_one.append(l)
        for l in t:
            if l == "#":
                if stack_two:
                    stack_two.pop()
            else:
                stack_two.append(l)
        
        return stack_one == stack_two