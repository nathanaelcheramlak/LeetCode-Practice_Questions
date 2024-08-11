class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for num in range(left, right + 1):
            is_in = False
            for interval in ranges:
                if interval[1] >= num and interval[0] <= num:
                    is_in = True
                    break
            if not is_in:
                return False
        return True