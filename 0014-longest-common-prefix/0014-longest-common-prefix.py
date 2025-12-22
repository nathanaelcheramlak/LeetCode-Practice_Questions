class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            curr_prefix = []
            for i in range(min(len(prefix), len(s))):
                if s[i] == prefix[i]:
                    curr_prefix.append(s[i])
                else:
                    break
            prefix = curr_prefix
        
        return "".join(prefix)