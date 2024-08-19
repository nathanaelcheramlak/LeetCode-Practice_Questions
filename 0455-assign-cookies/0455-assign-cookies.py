class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0

        while content_children < len(g) and cookie_index < len(s):
            if g[content_children] <= s[cookie_index]:
                content_children += 1

            cookie_index += 1
        
        return content_children
    # Time Complexity: O(nlog(n) + mlog(m)) -- Due to Sorting
    # Space Complexity: O(m+n) -- Due to python .sort() method
            