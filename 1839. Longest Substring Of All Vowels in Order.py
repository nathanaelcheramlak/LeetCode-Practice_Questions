# Problem #1839

"""
A string is considered beautiful if it satisfies the following conditions:
Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.
Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
"""

def longestBeautifulSubstring(word):
    max_beauties = 0
    mx = 1
    vowels = {'a', 'e', 'i', 'o', 'u'}

    p1 = 0
    p2 = 1
    while p2 < len(word):
        if word[p2] >= word[p2-1]:
            mx += 1
        else:
            if mx > max_beauties and set(word[p1:p2]) == vowels:
                max_beauties = mx
            mx = 1
        p2 += 1
        p1 = p2 - mx

    if mx > max_beauties and set(word[p1:p2]) == vowels:
        max_beauties = mx

    return max_beauties
    
# Time Complexity: O(N)
# Space Complexity: O(1)
        
        
            