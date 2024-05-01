class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        l_word = list(word)
        
        p1 = 0
        try:
            p2 = l_word.index(ch)
        except:
            return word
        
        while p2 >= p1:
            l_word[p1], l_word[p2] = l_word[p2], l_word[p1]
            p1 += 1
            p2 -= 1
        return "".join(l_word)
            