class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if needle[0] == haystack[i]:
                is_found = True
                for j in range(1, len(needle)):
                    if needle[j] != haystack[i+j]:
                        is_found = False
                        break
                if is_found:
                    return i
        return -1