class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = list(s[:2])
        for i in s[2:]:
            if ans[-1] == ans[-2] == i:
                continue
            else:
                ans.append(i)
        return ''.join(ans)
