class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        p1 = 0
        p2 = 0
        output = ""
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1] > word2[p2]:
                output += word1[p1]
                p1 += 1
            elif word1[p1] == word2[p2]:
                temp1, temp2 = p1, p2 
                while temp1 < len(word1) and temp2 < len(word2):
                    if word1[temp1] == word2[temp2]:
                        temp1 += 1
                        temp2 += 1
                    else:
                        break
                if temp1 == len(word1):
                    output += word1[p1:temp1]
                    p1 = temp1
                elif word1[temp1] > word2[temp2]:
                    output += word1[p1:temp1]
                    p1 = temp1
                else:
                    output += word2[p2:temp2]
                    p2 = temp2
            else:
                output += word2[p2]
                p2 += 1
        if p1 != len(word1):
            output += word1[p1:]
        else:
            output += word2[p2:]

        return output