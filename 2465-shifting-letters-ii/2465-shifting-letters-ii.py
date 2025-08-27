class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0] * len(s)
        for start, end, direction in shifts:
            if direction == 1:
                shift[start] += 1
                if end + 1 < len(s):
                    shift[end + 1] -= 1
            else:
                shift[start] -= 1
                if end + 1 < len(s):
                    shift[end + 1] += 1
        prefix = []
        acc = 0
        for sh in shift:
            acc += sh
            prefix.append(acc)

        ans = []
        for i in range(len(s)):
            new_l = chr(97 + (ord(s[i]) + prefix[i] - 97) % 26)
            ans.append(new_l)
        
        return "".join(ans)