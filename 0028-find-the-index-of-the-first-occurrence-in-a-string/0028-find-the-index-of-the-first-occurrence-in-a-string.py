class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        if len(needle) > len(haystack):
            return -1
        
        l = len(needle)

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: l+i] == needle:
                return i
        return -1
