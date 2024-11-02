class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        play = sentence[-1]
        sLst = sentence.split(' ')
        for l in sLst:
            if l[0] != play:
                return False
            play = l[-1]
        return True