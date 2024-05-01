class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return 1
        left = 2
        right = num // 2
        while right >= left:
            mid = (right + left) // 2
            if mid**2 > num:
                right = mid - 1
            elif mid**2 < num:
                left = mid + 1
            else:
                return True
            
        return False