class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        i = len(arr) - 1
        maxElement = arr[i]
        result = [0 for _ in range(len(arr))]

        while i >= 0:
            if i == len(arr) - 1:
                result[i] = -1
            elif arr[i] >= maxElement:
                result[i] = maxElement
                maxElement = arr[i]
            else:
                result[i] = maxElement
            i -= 1
        return result