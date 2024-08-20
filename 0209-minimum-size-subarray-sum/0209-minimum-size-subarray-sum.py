class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        
        left = 0
        right = 0
        minimum = len(nums)
        current_sum = nums[left]
        while right < len(nums):
                
            if current_sum < target:
                right += 1
                if right < len(nums):
                    current_sum += nums[right]
            else:
                minimum = min(minimum, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return minimum
    # Time Complexity: O(n)
    # Space Complexity: O(1)