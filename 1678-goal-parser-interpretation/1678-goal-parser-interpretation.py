class Solution:
    def interpret(self, s: str) -> str:
        i = 0
        result = []
        while i < len(s):
            if s[i] == "G":
                result.append("G")
                i += 1
            elif s[i] == "(" and s[i+1] == ")":
                result.append("o")
                i += 2
            else:
                result.append("al")
                i += 4
        return "".join(result)