class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = 0
        result = []

        while right < len(s):
            if s[left] == ' ':
                left += 1
                right += 1
            else: 
                right += 1
                if right < len(s) and s[right] == ' ':
                    result.append(s[left:right])
                    right += 1
                    left = right

        if s[right-1] != ' ':
            result.append(s[left:right])

        answer = ' '.join(result[::-1])
        return answer
