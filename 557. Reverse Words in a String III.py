# Problem #557

"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

def reverseWords(s):
    l = s.split(' ')
    for i in range(len(l)):
        l[i] = l[i][::-1]
    return ' '.join(l)
        
# Time Complexity: O(M + N) M->Size of 'l', N->Size of 's'
# Space Complexity: O(N)