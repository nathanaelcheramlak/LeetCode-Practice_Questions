class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
        gp = 0
        sp = 0
        count = 0
        while gp < len(g) and sp < len(s):
            if g[gp] > s[sp]:
                sp += 1
            else:
                gp += 1
                sp += 1
                count += 1
        
        return count
            