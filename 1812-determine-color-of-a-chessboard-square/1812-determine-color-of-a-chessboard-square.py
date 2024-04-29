class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        if ( ord(coordinates[0]) + int(coordinates[-1]) ) % 2 == 0:
            return False
        return True