class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypt = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                decrypt.append(chr(96 + int(s[i-2:i])))
                i -= 3
            else:
                decrypt.append(chr(int(s[i]) + 96))
                i -= 1
        return ''.join(decrypt[::-1])