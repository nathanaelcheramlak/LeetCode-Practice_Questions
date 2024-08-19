class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left].lower() not in vowels:
                left += 1
            if s[right].lower() not in vowels:
                right -= 1
                
            if s[right].lower() in vowels and s[left].lower() in vowels:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1
        
        return "".join(s)
            