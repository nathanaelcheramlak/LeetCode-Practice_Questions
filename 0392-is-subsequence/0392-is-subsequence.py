class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        for letter in t:
            if sp < len(s) and letter == s[sp]:
                sp += 1
            if sp == len(s):
                return True
        return sp == len(s)