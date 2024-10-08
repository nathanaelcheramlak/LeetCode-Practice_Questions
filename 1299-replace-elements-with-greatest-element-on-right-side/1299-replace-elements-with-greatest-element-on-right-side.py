class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_element = -1
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = max_element
            
            if current > max_element:
                max_element = current
                
        return arr