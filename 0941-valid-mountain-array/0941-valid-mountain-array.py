class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        peak_counter = 0
        
        if arr[1] < arr[0]:
            return False
        is_increasing = True
        
        for i in range(len(arr)-1):
            diff = arr[i + 1] - arr[i]
            if diff <= 0 and peak_counter == 0:
                peak_counter += 1
                is_increasing = False
            if diff <= 0 and is_increasing:
                return False
            if diff >= 0 and not is_increasing:
                return False
        return True and peak_counter == 1