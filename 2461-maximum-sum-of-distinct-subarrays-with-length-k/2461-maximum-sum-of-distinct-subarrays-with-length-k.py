class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = 0
        temp = sum(nums[:k])
        map = Counter(nums[:k])
        if len(map) == k:
            maxi = max(maxi, temp)
        for i in range(1, len(nums) - k + 1):
            temp += nums[i+k-1]
            temp -= nums[i-1]
            if map[nums[i-1]] == 1:
                del map[nums[i-1]]
            else: 
                map[nums[i-1]] -= 1
            
            if nums[i+k-1] in map:
                map[nums[i+k-1]] += 1
            else: 
                map[nums[i+k-1]] = 1

            if len(map) == k:
                maxi = max(maxi, temp)

        return maxi