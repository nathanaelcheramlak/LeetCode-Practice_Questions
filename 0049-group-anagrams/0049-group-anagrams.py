class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for letter in word:
                idx = ord(letter) - ord("a")
                char_count[idx] += 1
            count_tup = tuple(char_count)
            hash_map[count_tup].append(word)
        
        return list(hash_map.values())