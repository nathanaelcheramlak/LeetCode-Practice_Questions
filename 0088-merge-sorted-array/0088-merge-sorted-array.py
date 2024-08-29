class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Bruteforce
        i = 0
        while m < len(nums1):
            nums1[m] = nums2[i]
            i += 1
            m += 1
            
        return nums1.sort()