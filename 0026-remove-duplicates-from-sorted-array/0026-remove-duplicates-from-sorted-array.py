class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1 = 1
        while p1 < len(nums):
            if nums[p1] == nums[p1-1]:
                nums.pop(p1)
            else:
                p1 += 1
        return len(nums)
                
            