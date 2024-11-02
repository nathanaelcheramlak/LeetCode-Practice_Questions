class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        largest = ''.join(nums)

        if largest[0] == '0':
            return '0'
        return largest