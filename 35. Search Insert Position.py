# Problem 35 - Search Insert Position
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
"""

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2
    while right >= left:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid
    if target > nums[mid]:
        return mid + 1
    return mid

# Time Complexity: O(log(n))
# Space Complexity: O(1)