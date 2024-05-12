class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        counter = 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                c = 0
            if counter < c:
                counter = c
        return counter
            