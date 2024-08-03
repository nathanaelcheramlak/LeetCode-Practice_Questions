class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        lst = list()
        for n in range(lo, hi+1):
            num = n
            counter = 0
            while n != 1:
                counter += 1
                if n % 2 == 0:
                    n /= 2
                else:
                    n = 3 * n + 1
            lst.append([counter, num])
        lst.sort()
        return lst[k-1][1]
        