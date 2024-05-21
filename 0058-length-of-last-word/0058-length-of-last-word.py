class Solution(object):
    def lengthOfLastWord(self, word):
        """
        :type s: str
        :rtype: int
        """
        isSpace = True
        l = len(word) - 1
        lastW = 0

        while l >= 0:
            if word[l] != ' ':
                lastW += 1
                isSpace = False  
            elif not isSpace and lastW > 0:
                break
            l -= 1

        return lastW