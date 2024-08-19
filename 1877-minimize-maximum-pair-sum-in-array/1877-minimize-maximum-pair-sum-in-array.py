class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_pair = 0
        left = 0
        right = len(nums) - 1
        while right > left:
            current_sum = nums[left] + nums[right]
            if current_sum > max_pair:
                max_pair = current_sum
            left += 1
            right -= 1
        
        return max_pair