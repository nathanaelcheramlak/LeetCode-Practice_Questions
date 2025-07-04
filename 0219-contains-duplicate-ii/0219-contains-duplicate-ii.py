class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k > len(nums) - 1 and len(set(nums)) != len(nums):
            return True
        
        myset = set(nums[:k + 1])
        for i in range(len(nums) - k):
            if len(myset) != k + 1:
                return True
            myset.discard(nums[i])
            if i + k + 1 < len(nums):
                myset.add(nums[i + k + 1])
        
        return False