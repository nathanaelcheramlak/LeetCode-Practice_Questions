class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = 10
        hashmap = dict()
        jout = []
        for i in range(len(s) - k):
            window = s[i: i+k]
            if window not in hashmap:
                hashmap[window] = 1
            else:
                hashmap[window] += 1
                if hashmap[window] == 2:
                    jout.append(window)
        return jout