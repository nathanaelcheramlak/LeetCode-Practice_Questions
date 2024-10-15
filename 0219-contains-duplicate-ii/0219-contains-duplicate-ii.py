class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        for i in range(k + 1):
            if i < len(nums):
                if nums[i] in hashmap: return True
                else: hashmap[nums[i]] = 1
            else: return False

        for i in range(k + 1, len(nums)):
            # Remove 
            if nums[i - k - 1] in hashmap and hashmap[nums[i - k - 1]] == 1:
                hashmap.pop(nums[i - k - 1])
            
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = 1
        
        return False