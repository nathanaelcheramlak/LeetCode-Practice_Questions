class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        grouped_ls = []
        for st in strs:
            sorted_st = "".join(sorted(st))
            if sorted_st not in dic:
                dic[sorted_st] = [st]
            else:
                dic[sorted_st].append(st)
        for value in dic.values():
            grouped_ls.append(value)
        return grouped_ls
                