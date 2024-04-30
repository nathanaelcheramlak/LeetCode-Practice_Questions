class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        
        n = num % 9
        if n == 0:
            return 9
        return n