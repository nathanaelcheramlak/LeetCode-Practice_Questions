class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
    
        max_ascii = ord(s[0])
        for letter in s:
            if ord(letter) < max_ascii:
                return False
            max_ascii = ord(letter)
        return True