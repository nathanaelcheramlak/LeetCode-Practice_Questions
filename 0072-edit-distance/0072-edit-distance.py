class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        cache = {}
        def edit(i, j):
            if i == n1 or j == n2:
                return max(n1 - i, n2 - j)
            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                cache[(i, j)] = edit(i + 1, j + 1)
            else:
                cache[(i, j)] = min(1 + edit(i, j + 1), 1 + edit(i + 1, j), 1 + edit(i + 1, j + 1))
            
            return cache[(i, j)]
        
        return edit(0, 0)