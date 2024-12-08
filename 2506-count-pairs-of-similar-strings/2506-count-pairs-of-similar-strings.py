class Solution:
    def similarPairs(self, words: List[str]) -> int:
        map = dict()
        count = 0
        for word in words:
            sorted_chars = ''.join(sorted(set(word)))
            map[sorted_chars] = map.get(sorted_chars, 0) + 1

        for val in map.values():
            count += (val * (val - 1)) // 2
        
        return count