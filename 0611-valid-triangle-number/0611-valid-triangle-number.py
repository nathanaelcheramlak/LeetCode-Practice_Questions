class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        triangle_count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                idx = bisect_left(nums, nums[i] + nums[j])
                triangle_count += max(0, idx - 1 - j)
        
        return triangle_count