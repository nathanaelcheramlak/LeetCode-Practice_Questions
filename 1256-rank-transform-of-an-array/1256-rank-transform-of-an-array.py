class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {}
        rank = 1
        sorted_arr = sorted(arr)

        for num in sorted_arr:
            if num not in dic:
                dic[num] = rank
                rank += 1
        
        ans = []
        for num in arr:
            ans.append(dic[num])
        
        return ans