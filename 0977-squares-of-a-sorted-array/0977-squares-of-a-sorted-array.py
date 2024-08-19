class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Using the two-pointer approach
        left = 0
        right = len(nums) - 1
        result = list()
        
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[right] ** 2)
                right -=1
            else:
                result.append(nums[left] ** 2)
                left += 1
        result.reverse() # Reverse in-place without using extra space
        
        return result
        
    # Time Complexity: O(n)
    # Space Complexity: O(1)