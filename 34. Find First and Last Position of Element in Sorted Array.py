# Problem #34
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

def searchRange(nums, target):
        indices = []
        for i in range(len(nums)):
            if nums[i] == target:
                indices.append(i)
        if len(indices) == 1:
            return [indices[0], indices[0]]
        elif len(indices) < 1:
            return [-1,-1]
        return [indices[0], indices[-1]]

# Time Complexity: O(N)
# Space Complexity: O(N)