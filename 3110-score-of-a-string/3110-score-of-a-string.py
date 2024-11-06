class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        prev = ord(s[0])
        for l in s[1:]:
            score += (abs(prev - ord(l)))
            prev = ord(l)
        return score