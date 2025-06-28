class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_major = nums[0]
        major_freq = 1

        for element in nums[1:]:
            if major_freq == 0:
                current_major = element

            if current_major == element:
                major_freq += 1
            else:
                major_freq -= 1
            
        return current_major