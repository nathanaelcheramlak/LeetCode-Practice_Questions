class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        idx = []
        result = []
        for i in range(len(nums)):
            if nums[i] == x:
                idx.append(i)

        for q in queries:
            q -= 1
            if q >= len(idx):
                result.append(-1)
            else:
                result.append(idx[q])
        
        return result
