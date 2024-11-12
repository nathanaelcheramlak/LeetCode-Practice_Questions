class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count = "1"
        for i in range(n-1):
            temp = ""
            c = 1
            current = count[0]
            for j in range(1, len(count)):
                if count[j] == current:
                    c += 1
                else:
                    temp += str(c) + current
                    c = 1
                    current = count[j]
            temp += str(c) + current
            count = temp
        return count
         