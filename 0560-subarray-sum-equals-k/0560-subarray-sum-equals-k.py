class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = { 0: 1 }
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            if prefix - k in hashmap:
                result += hashmap[prefix - k]

            hashmap[prefix] = hashmap.get(prefix, 0) + 1
        
        return result