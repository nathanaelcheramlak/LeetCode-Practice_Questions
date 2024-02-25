# Problem #1

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):
    # Stores Value and Index from nums 
    value_index = {}

    for i in range(len(nums)):
        difference = target - nums[i]

        # Checks if the difference exists, and if it does we have found the two numbers.
        if difference in value_index:
            return [i, value_index[difference]]
        
        # If the above condition fail, we will add a new element to our dictionary above.
        value_index[nums[i]] = i
    return []
