class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            char_count = Counter(word)
            count_list = []
            for alp in string.ascii_lowercase:
                freq = char_count[alp]
                count_list.append(freq)
            count_tup = tuple(count_list)
            hash_map[count_tup].append(word)
        
        return list(hash_map.values())