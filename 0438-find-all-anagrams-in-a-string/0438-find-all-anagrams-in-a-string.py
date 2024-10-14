class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        valid_anagrams = []
        p_map = dict()
        for letter in p:
            if letter not in p_map:
                p_map[letter] = 1
            else:
                p_map[letter] += 1

        k = len(p)
        sliding_map = dict()
        for letter in s[0:k]:
            if letter not in sliding_map:
                sliding_map[letter] = 1
            else:
                sliding_map[letter] += 1

        if sliding_map == p_map:
            valid_anagrams.append(0)

        for i in range(k, len(s)):
            # Addition
            if s[i] in sliding_map:
                sliding_map[s[i]] += 1
            else:
                sliding_map[s[i]] = 1

            # Removal
            if s[i - k] in sliding_map and sliding_map[s[i - k]] >= 2:
                sliding_map[s[i - k]] -= 1
            else:
                sliding_map.pop(s[i - k])
            
            if sliding_map == p_map:
                valid_anagrams.append(i - k + 1)
        
        return valid_anagrams