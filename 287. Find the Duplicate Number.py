# Problem Number # 287
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
"""

def findDuplicate(nums):
    map = dict()
    for n in nums:
        if n not in map:
            map[n] = 1
        else:
            return n
    return None

# Time Complexity: O(N)
# Space Complexity: O(N)