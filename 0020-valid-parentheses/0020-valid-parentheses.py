class Solution(object):
    def isValid(self, parent):
        """
        :type s: str
        :rtype: bool
        """
        mapper = {']':'[', '}':'{', ')':'('}
        stack = []

        for char in parent:
            if char in mapper.values():
                stack.append(char)
            if char in mapper:
                if stack and stack[-1] == mapper[char]:
                    stack.pop()
                else:
                    return False

        return not stack