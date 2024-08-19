class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        is_seen = dict()
        while True:
            if n == 1:
                return True
            if n not in is_seen:
                is_seen[n] = 0
                digits = str(n)
                n = 0
                for digit in digits:
                    n += int(digit) ** 2
            else:
                return False
        return False
                