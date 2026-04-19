class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        max_len = 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if ptr1 > ptr2:
                ptr2 = ptr1
                if ptr2 >= len(nums2): break
            # Invalid
            if nums1[ptr1] > nums2[ptr2]:
                ptr1 += 1
            # Valid
            else:
                max_len = max(max_len, ptr2 - ptr1)
                ptr2 += 1
        
        return max_len