class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        last = nums[0]
        count = 0
        n = 0
        while n < l:
            if nums[n] == last:
                count += 1
            else:
                count = 1
                last = nums[n]

            if count > 2:
                nums.pop(n)
                l -= 1
                continue
            n += 1