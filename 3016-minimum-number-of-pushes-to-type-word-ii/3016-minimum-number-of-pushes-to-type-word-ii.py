class Solution:
    def minimumPushes(self, word: str) -> int:
        hashmap = dict()
        for letter in word:
            if letter not in hashmap:
                hashmap[letter] = 1
            else: 
                hashmap[letter] += 1

        sorted_map = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        print(sorted_map)
        multiplier = 0
        i = 0
        output = 0
        for val in sorted_map.values():
            if i % 8 == 0:
                multiplier += 1
            output += (val * multiplier)
            i += 1
        return output
