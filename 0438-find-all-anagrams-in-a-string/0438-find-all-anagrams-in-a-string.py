class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        out = []
        left = 0
        right = len(p) - 1
        
        p = sorted(p)
        
        while right < len(s):
            window = s[left:right+1]
            if sorted(window) == p:
                out.append(left)
            left += 1
            right += 1
        return out